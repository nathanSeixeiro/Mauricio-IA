import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

load_dotenv()
 
# Constants for environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AZURE_AI_SEARCH_ENDPOINT = os.getenv("AZURE_AI_SEARCH_ENDPOINT")
AZURE_AI_SEARCH_INDEX = os.getenv("AZURE_AI_SEARCH_INDEX")
AZURE_AI_SEARCH_API_KEY = os.getenv("AZURE_AI_SEARCH_API_KEY")
 
if not all([GEMINI_API_KEY, AZURE_AI_SEARCH_ENDPOINT, AZURE_AI_SEARCH_INDEX, AZURE_AI_SEARCH_API_KEY]):
    raise Exception("Uma ou mais variáveis de ambiente não foram carregadas corretamente.")
 
def get_language_model(model_type):
    if model_type == 'gemini':
        return ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0.5,
            top_p=0.95,
            top_k=64,
            max_output_tokens=8192,
            response_mime_type="text/plain",
            google_api_key=GEMINI_API_KEY
        )
    elif model_type == 'openai':
        return ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.5,
            api_key=OPENAI_API_KEY
        )
    else:
        raise ValueError(f"Unknown model type: {model_type}")

