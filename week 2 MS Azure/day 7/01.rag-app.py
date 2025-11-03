import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_AI_SEARCH_ENDPOINT = os.getenv("AZURE_AI_SEARCH_ENDPOINT")
AZURE_AI_SEARCH_API_KEY = os.getenv("AZURE_AI_SEARCH_API_KEY")
DEPLOYMENT_NAME = os.getenv("DEPLOYMENT_NAME")
DEPLOYMENT_EMBEDDING_NAME = os.getenv("DEPLOYMENT_EMBEDDING_NAME")
INDEX_NAME = "hotel-vector"

chat_client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version="2024-12-01-preview",
)

prompt =[
    {"role": "system", 
     "content": "You are a helpful assistant that helps people find information."},
]

input_text = input("Enter your question: ")
prompt.append({"role": "user", "content": input_text})

# Azure AI Search parameters
rag_params = {
    "data_sources": [
        {
            # he following params are used to search the index
            "type": "azure_search",
            "parameters": {
                "endpoint": AZURE_AI_SEARCH_ENDPOINT,
                "index_name": INDEX_NAME,
                "authentication": {
                    "type": "api_key",
                    "key": AZURE_AI_SEARCH_API_KEY,
                },
                # The following params are used to vectorize the query
                "query_type": "vector",
                "embedding_dependency": {
                    "type": "deployment_name",
                    "deployment_name": DEPLOYMENT_EMBEDDING_NAME,
                },
            }
        }
    ],
}

response = chat_client.chat.completions.create(
    model=DEPLOYMENT_NAME,
    messages=prompt,
    extra_body=rag_params
)

print("Response:")
print(response.choices[0].message.content)