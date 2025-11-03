from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

load_dotenv()

llm = AzureChatOpenAI(model="dev-gpt-4.1-mini", temperature=0.8)

response = llm.invoke("삼성전자의 파운드리 사업에 대해서 알려줘")
print(response.content)