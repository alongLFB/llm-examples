import streamlit as st
from langchain.llms import OpenAI

st.title("🦜🔗 Langchain Quickstart App")

with st.sidebar:
    openai_api_base = st.secrets.openai_base
    openai_api_key = st.secrets.openai_key
    # "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"


def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key, openai_api_base=openai_api_base)
    st.info(llm(input_text))


with st.form("my_form"):
    text = st.text_area("Enter text:", "What are 3 key advice for learning how to code?")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        generate_response(text)
