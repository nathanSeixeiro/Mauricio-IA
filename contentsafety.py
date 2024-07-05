import os
from azure.ai.contentsafety import ContentSafetyClient
from azure.ai.contentsafety.models import TextCategory
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError
from azure.ai.contentsafety.models import AnalyzeTextOptions

def analyze_text(query):
    # Retrieve the endpoint URL and key from environment variables
    endpoint_url = os.getenv("AZURE_AI_CONTENT_SAFETY_ENDPOINT")
    key = os.getenv("AZURE_AI_CONTENT_SAFETY_KEY")

    # Create a Content Safety client using the endpoint URL and key
    client = ContentSafetyClient(endpoint_url, AzureKeyCredential(key))

    # Construct a request object with the text to be analyzed
    request = AnalyzeTextOptions(text=query["content"])

    # Analyze the text
    try:
        response = client.analyze_text(request)
    except HttpResponseError as e:
        # Handle errors during the text analysis process
        print("Analyze text failed.")
        if e.error:
            print(f"Error code: {e.error.code}")
            print(f"Error message: {e.error.message}")
            raise
        print(e)
        raise

    # Extract analysis results for specific categories
    hate_result = next(item for item in response.categories_analysis if item.category == TextCategory.HATE)
    self_harm_result = next(item for item in response.categories_analysis if item.category == TextCategory.SELF_HARM)
    sexual_result = next(item for item in response.categories_analysis if item.category == TextCategory.SEXUAL)
    violence_result = next(item for item in response.categories_analysis if item.category == TextCategory.VIOLENCE)

    # Print severity levels for each category if they exist
    if hate_result:
        print(f"Hate severity: {hate_result.severity}")
    if self_harm_result:
        print(f"SelfHarm severity: {self_harm_result.severity}")
    if sexual_result:
        print(f"Sexual severity: {sexual_result.severity}")
    if violence_result:
        print(f"Violence severity: {violence_result.severity}")
    
    #checks whether the content is harmful
    if hate_result.severity+self_harm_result.severity+sexual_result.severity+violence_result.severity <= 0:
        return False

    #Return reslts content safety
    return [hate_result,self_harm_result,sexual_result,violence_result]