import openai
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")

st.title("Welcome to the AI Poem Generator")
st.write("Ask me anything, and I'll respond with a poem!")
subject = st.text_input("시의 주제를 입력하세요: ")
content = st.text_area("시의 내용을 입력하세요: ")

button_clicked = st.button("시 생성하기")

if button_clicked:
    messages = [
        {"role": "system", "content": "You are a AI poem."},
        {"role": "user", "content": f"주제: {subject}, 내용: {content}로 시를 작성해줘."}
    ]

    with st.spinner("Wait for it..."):
        response = openai.chat.completions.create(
                        model="dev-gpt-4.1-mini",
                        messages=messages,
                        temperature=0.8
                    )

    st.write(response.choices[0].message.content)