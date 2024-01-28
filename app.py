# Q&A Chatbot
from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os

# Function to load OpenAI model and get responses

def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY") , model_name='gpt-3.5-turbo-instruct', temperature=0.6)
    response = llm(question)
    return response


### initialize our streamlit app

st.set_page_config(page_title="Q&A Chatbot", page_icon=":robot_face:", layout="wide")
st.header("Langchain Appication")

input=st.text_input("Input: ", key="input")
response=get_openai_response(input)

submit = st.button("Ask the question")

if submit:
    st.subheader("The response is")
    st.write(response)

