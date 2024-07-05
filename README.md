# Documento Descritivo para Prova de Conceito (POC) - Utilizando Inteligência Artificial

## Nome dos Integrantes:
- Lucas da Silva de Souza
- Nathan Victor Rodrigues Seixeiro
- Rafael Santos Neves

## Atividade de Cada Integrante:
- **Lucas da Silva de Souza:** Implementou todo o sistema em uma aplicação web, realizando o frontend e o backend e auxiliando no filtro de conteúdo para retornar dados mais precisos da IA.
- **Nathan Victor Rodrigues Seixeiro:** Desenvolveu a integração com a API do ChatGoogleGenerativeAI e OpenAI no LangChain, configurou o Azure AI Search e desenvolveu a função de busca no Azure, a memória de conversação e a cadeia de conversação a partir de sumário. Também cuidou da documentação e organização dos passos.
- **Rafael Santos Neves:** Desenvolveu a lógica de sinônimos, implementação do LangChain, auxiliou na criação do serviço do Azure AI Search, treinou e melhorou a assertividade dos resultados com técnicas de engenharia de prompt e dos testes de assertividade e aprimorou os resultados esperados com Azure Content Safety. 

## Descrição da Aplicação:
A aplicação desenvolvida é um chatbot inteligente que combina a busca em um índice de inteligência artificial da Azure com a geração de respostas utilizando modelos de linguagem, inicialmente da Google Generative AI (usando o modelo Gemini-1.5-flash). A principal funcionalidade da aplicação é permitir a busca de informações relevantes em documentos armazenados na Azure e, em seguida, gerar respostas contextualizadas utilizando IA avançada.

### Problema que Resolve:
A aplicação resolve o problema de encontrar e sintetizar informações de grandes volumes de dados textuais, facilitando a obtenção de respostas rápidas e precisas a partir de documentos armazenados.

### Como Funciona:
1. **Entrada do Usuário:** O usuário insere uma consulta de busca.
2. **Geração de Sinônimos:** A consulta é processada para gerar sinônimos utilizando o modelo de linguagem.
3. **Busca na Azure:** Os sinônimos gerados são utilizados para buscar informações relevantes no índice da Azure.
4. **Combinação de Resultados:** Os resultados da busca são combinados com a consulta original do usuário para formar um contexto.
5. **Geração de Resposta:** A resposta final é gerada pelo modelo de linguagem Google Generative AI, utilizando o contexto combinado.

## Instruções de Uso:

### Requisitos:
- Python 3.9 ou superior
- Conta no Google Cloud com acesso ao serviço Google Generative AI (Gemini)
- Conta no Google Cloud com acesso ao serviço da OpenAI
- Conta no Azure com acesso ao serviço Azure Cognitive Search
- Conta no Azure com acesso ao serviço Azure Blob Storage
- Bibliotecas do arquivo `requirements.txt`

### Instalação:
1. **Clone o repositório:**
    ```bash
    git clone https://github.com/nathanSeixeiro/Mauricio-IA.git
    cd Mauricio-IA
    ```

2. **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate   # Para Linux/MacOS
    venv\Scripts\activate      # Para Windows
    ```

3. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure as variáveis de ambiente:**
    - Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:
        ``` 
        GEMINI_API_KEY=<your-gemini-api-key>
        OPENAI_API_KEY=<your-openai-api-key>
        AZURE_AI_SEARCH_ENDPOINT=<your-search-endpoint>
        AZURE_AI_SEARCH_INDEX=<your-search-index-name>
        AZURE_AI_SEARCH_API_KEY=<your-search-api-key>
        AZURE_AI_CONTENT_SAFETY_ENDPOINT=<your-content-safety-endpoint>
        AZURE_AI_CONTENT_SAFETY_KEY=<your-content-safety-key>
        ```

### Execução:
1. **Inicie a aplicação:**
    ```bash
    python app.py
    ```

2. **Utilize a aplicação:**
    - Abra o arquivo index.html e faça uma pergunta no prompt relacionado aos documentos armazenados.

## Descrição das Ferramentas Utilizadas:

- **ChatGoogleGenerativeAI (modelo Gemini-1.5-flash):** Modelo de linguagem desenvolvido pela Google, utilizado para gerar sinônimos e respostas contextualizadas.
- **OpenAI (modelo GPT-3.5-turbo):** Utilizado para complementar a geração de respostas com alta precisão.
- **Azure Cognitive Search:** Serviço de busca inteligente da Azure, utilizado para indexar e buscar informações relevantes a partir de documentos.
- **LangChain:** Biblioteca para construir cadeias de modelos de linguagem, utilizada para configurar e gerenciar as interações com os modelos.
- **Azure Content Safety:** Serviço da Azure utilizado para garantir que os resultados gerados estejam em conformidade com as políticas de segurança de conteúdo.
- **Flask:** Framework web utilizado para desenvolver o backend da aplicação.
