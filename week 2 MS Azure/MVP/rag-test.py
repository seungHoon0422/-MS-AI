import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

AZURE_OPENAI_ENDPOINT = "<your-azure-openai-endpoint>"
AZURE_OPENAI_API_KEY = "<your-azure-openai-api-key>"
AZURE_AI_SEARCH_ENDPOINT = "<your-azure-ai-search-endpoint>"
AZURE_AI_SEARCH_API_KEY = "<your-azure-ai-search-api-key>"
DEPLOYMENT_NAME = "<your-deployment-name>"
DEPLOYMENT_EMBEDDING_NAME = "<your-deployment-embedding-name>"
INDEX_NAME = "<your-index-name>"

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
                "query_type": "simple",
                # "embedding_dependency": {
                #     "type": "deployment_name",
                #     "deployment_name": DEPLOYMENT_EMBEDDING_NAME,
                # },
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