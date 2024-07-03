# Documento Descritivo para Prova de Conceito (POC) - Utilizando Inteligência Artificial

## Nome dos Integrantes:
- Lucas da Silva de Souza
- Nathan Victor Rodrigues Seixeiro
- Rafael Santos Neves

## Atividade de Cada Integrante:
- **Lucas da Silva de Souza:** Implementou ...

- **Nathan Victor Rodrigues Seixeiro:** Desenvolveu a integração com a API do ChatGoogleGenerativeAI no langChain, Configurou o Azure AI Search e desenvolveu a função de busca no Azure, a memória de conversação e a cadeia de conversação com sumário. Também cuidou da documentação.

- **Rafael Santos Neves:** Desenvolveu a lógica de sinônimos, implementação do langchain, auxilio na crição do serviço do Azure AI Search, treinou e melhorou a assertividade dos resultados com técnicas de engenharia de prompt e dos testes de assertividade. 

## Descrição da Aplicação:
A aplicação desenvolvida é um chatbot inteligente que combina a busca em um índice de inteligência artificial da Azure com a geração de respostas utilizando o modelo de linguagem da Google Generative AI (usando o model Gemini-1.5-flash). A principal funcionalidade da aplicação é permitir a busca de informações relevantes em documentos armazenados na Azure e, em seguida, gerar respostas contextualizadas utilizando IA avançada.

### Problema que Resolve:
A aplicação resolve o problema de encontrar e sintetizar informações de grandes volumes de dados textuais, facilitando a obtenção de respostas rápidas e precisas a partir de documentos armazenados na Azure.

### Como Funciona:
1. **Entrada do Usuário:** O usuário insere uma consulta de busca.
2. **Geração de Sinônimos:** A consulta é processada para gerar sinônimos utilizando o modelo de linguagem Google Generative AI.
3. **Busca na Azure:** Os sinônimos gerados são utilizados para buscar informações relevantes no índice da Azure.
4. **Combinação de Resultados:** Os resultados da busca são combinados com a consulta original do usuário para formar um contexto.
5. **Geração de Resposta:** A resposta final é gerada pelo modelo de linguagem Google Generative AI, utilizando o contexto combinado.

## Instruções de Uso:

### Requisitos:
- Python 3.8 ou superior
- Conta no Google Cloud com acesso ao serviço Google Generative AI (Gemini)
- Conta no Azure com acesso ao serviço Azure Cognitive Search
- Biblioteca `langchain`
- Biblioteca `langchain_google_genai`
- Biblioteca `python-dotenv`
- Biblioteca `requests`
- Biblioteca `azure-core`
- Biblioteca `azure-search-documents`

### Instalação:
1. **Clone o repositório:**
    ```bash
    git clone <URL-do-repositório>
    cd <nome-do-repositório>
    ```

2. **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv env
    source env/bin/activate   # Para Linux/MacOS
    env\Scripts\activate      # Para Windows
    ```

3. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure as variáveis de ambiente:**
    - Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:
        ```
        GEMINI_API_KEY=your_gemini_api_key
        AZURE_AI_SEARCH_ENDPOINT=your_azure_search_endpoint
        AZURE_AI_SEARCH_INDEX=your_azure_search_index
        AZURE_AI_SEARCH_API_KEY=your_azure_search_api_key
        ```

### Execução:
1. **Inicie a aplicação:**
    ```bash
    python main.py
    ```

2. **Utilize a aplicação:**
    - Insira uma consulta no prompt e pressione Enter.
    - Para sair, digite 'sair', 'exit' ou 'quit'.

## Descrição das Ferramentas Utilizadas:

- **ChatGoogleGenerativeAI (Gemini-1.5-flash):** Modelo de linguagem desenvolvido pela Google, utilizado para gerar sinônimos e respostas contextualizadas.
- **Azure Cognitive Search:** Serviço de busca inteligente da Azure, utilizado para indexar e buscar informações relevantes a partir de documentos.
- **LangChain:** Biblioteca para construir cadeias de modelos de linguagem, utilizada para configurar e gerenciar as interações com o ChatGoogleGenerativeAI.
- **Dotenv:** Biblioteca para carregar variáveis de ambiente a partir de um arquivo `.env`.
- **Requests:** Biblioteca para fazer requisições HTTP em Python.
- **Azure Search Documents:** Biblioteca da Azure para interagir com o serviço Azure Cognitive Search.
