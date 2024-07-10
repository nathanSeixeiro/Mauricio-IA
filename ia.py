import os
import model  
from langchain.globals import set_debug
from dotenv import load_dotenv, find_dotenv
from langchain.chains import ConversationChain
from azure.search.documents import SearchClient
from langchain.prompts import ChatPromptTemplate
from azure.core.credentials import AzureKeyCredential
from langchain.memory import ConversationSummaryMemory
from langchain.chains import SimpleSequentialChain, LLMChain

# Load environment variables
if not find_dotenv():
    raise Exception("Arquivo .env não encontrado.")
load_dotenv()
# set_debug(True)

# Constants for environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AZURE_AI_SEARCH_ENDPOINT = os.getenv("AZURE_AI_SEARCH_ENDPOINT")
AZURE_AI_SEARCH_INDEX = os.getenv("AZURE_AI_SEARCH_INDEX")
AZURE_AI_SEARCH_API_KEY = os.getenv("AZURE_AI_SEARCH_API_KEY")

if not all([GEMINI_API_KEY, AZURE_AI_SEARCH_ENDPOINT, AZURE_AI_SEARCH_INDEX, AZURE_AI_SEARCH_API_KEY]):
    raise Exception("Uma ou mais variáveis de ambiente não foram carregadas corretamente.")

# Configure LLM 
llm = model.get_language_model('gemini')  

# Configure AI Search
search_client = SearchClient(
    endpoint=AZURE_AI_SEARCH_ENDPOINT,
    index_name=AZURE_AI_SEARCH_INDEX,
    credential=AzureKeyCredential(AZURE_AI_SEARCH_API_KEY)
)

def azure_ai_search(query):
    """
    Searches the Azure AI index with the given query.
   
    Args:
        query (str): The search query.
   
    Returns:
        list: A list of search results.
    """
    try:
        results = search_client.search(search_text=query)
        return [result['merged_content'] for result in results]
    except Exception as e:
        print(f"Erro ao buscar no Azure AI Search: {e}")
        return []

# Create the prompt template for synonyms
template_synonyms = ChatPromptTemplate.from_messages([
    ("system", '''
        Quero que você atue como um emissor de sinônimos.
        Quero que você me de diversos sinônimos para <palavra>palavra</palavra>.
        Sua resposta deve apenas conter os sinônimos. Nada a mais e nada a menos.
        --------
        Exemplo:
        Entrada-User: carro
        Sua resposta: carro veiculo automóvel automotor
        Entrada-User: cachorro
        Sua resposta: cachorro canino pet
        --------------------------------------------
        O sinônimo não pode ser mais que uma palavra,
        pois será enviado para uma IA search e é necessário enviar uma resposta de uma palavra por vez que corresponda ao sinônimo.
        -------------------------
        Exemplo do que não fazer:
        Entrada-User: policia
        Sua resposta: força policial autoridade policial guarda polícia guarda municipal polícia federal polícia estadual polícia civil polícia militar
        Entrada-User: desenvolvedor
        Sua resposta: engenheiro de software desenvolvedor de software arquiteto de software
        ------------------
        Em vez disso faça:
        Sua resposta: força autoridade militar polícia guarda
        Sua resposta: software desenvolvedor
        -----------------------------------------------------------------------------------------------------
        Caso tenha mais de uma palavra, decida se elas são compostas ou se são separadas com base no contexto.
        Exemplo:
        Entrada-User: carro elétrico
        Sua resposta: veículo movido a eletricidade automóvel eletrico
        Entrada-User: cachorro banana relógio
        Sua resposta: canino pet fruta horas
    '''),
    ("human", "<palavra>{input}</palavra>")
])

# Create the chain for generating synonyms
chain_synonyms = LLMChain(prompt=template_synonyms, llm=llm)
synonyms_chain = SimpleSequentialChain(chains=[chain_synonyms], verbose=True)

def retrieve_and_generate(query):
    """
    Integrates the Azure AI search with the LLM to generate a response.
   
    Args:
        query (str): The input query.
   
    Returns:
        str: The generated response from the LLM.
    """
    # Get synonyms for the query
    result_synonyms = synonyms_chain.invoke(f'{query['content']}')
    synonyms = result_synonyms["output"]
    print("Sinônimos gerados: ", synonyms)
   
    # Search Azure AI with synonyms
    context = azure_ai_search(synonyms + query['content'])
    if not context:
        return "Nenhum resultado encontrado."
   
    # Combine context and query to generate the response
    combined_prompt = f"""
    <Contexto>
    {context} 
    </Contexto>
    ---------
    <Questão>
    {query}
    </Questão>
    ------------------------------------------------------------------
    Quero que você atue como um analista de documentos de uma empresa.
    Você deve fazer a analise do <Contexto> e fazer um resumo do arquivo correspondente a questão <Questão>
    --------
    Exemplo:
    <Contexto>
        Exemplo
    </Contexto>
    <Questão>
        Qual metodologia é usada?
    </Questão>
    <Resposta>
        Análise Documental como uma 
        metodologia de investigação científica que adota determinados procedimentos técnicos e 
        científicos com o intuito de examinar e compreender o teor de documentos dos mais 
        variados tipos, e deles, obter as mais significativas informações, conforme o problema de 
        pesquisa estabelecido.
    </Resposta>
    -----------------------------------------------------------------------------------------------------------------------
    Caso <Questão> não seja uma pergunta ou pedido, você deve repassar as informações do documento e fazer um resumo sobre.
    --------
    Exemplo:
    <Contexto>
        Exemplo
    </Contexto>
    <Questão>
        como consumir drogas
    </Questão>
    <Resposta>
        Sua pergunta não esta no contexto, por favor pesquise sobre algo dentro do contexto.
    </Resposta>
    --------
    Exemplo:
    <Contexto>
        Exemplo
    </Contexto>
    <Questão>
        como roubar
    </Questão>
    <Resposta>
        Sua pergunta não esta no contexto, por favor pesquise sobre algo dentro do contexto.
    </Resposta>
    --------
    Exemplo do que não fazer:
    <Contexto>
        Exemplo
    </Contexto>
    <Questão>
        banana
    </Questão>
    <Resposta>
        Resumo:
        Banana, pacoba ou pacova é uma pseudobaga da bananeira, uma planta herbácea vivaz acaule da família Musaceae. São cultivadas em 130 países. Originárias do sudeste da Ásia são atualmente cultivadas em praticamente todas as regiões tropicais do planeta.
    </Resposta>
    """
    # combined_prompt = f"Contexto: {context} \n Questão: {query}"
    response = llm.invoke(combined_prompt)
    return response.content

# Configure the conversation chain with SummaryMemory
memory = ConversationSummaryMemory(llm=llm, memory_size=5)
conversation_chain = ConversationChain(
    llm=llm,
    memory=memory
)
