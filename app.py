import os
import openai
import streamlit as st
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')

# configuring streamlit page settings
st.set_page_config(
    page_title="Summer School Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("Summer School Chatbot")
st.sidebar.markdown("Our Chatbot")

# create an input to store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# input field for user's message
user_prompt = st.chat_input("Ask Chatbot a Question...")

if user_prompt:
    # add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # send user's message to GPT-4o and get a response
    response = openai.ChatCompletion.create(
        #prompt_template = """""",
        model="gpt-4o",
        messages=[
            {"role": "system", "content": user_prompt},
            *st.session_state.chat_history
        ]
    )

    assistant_response = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    # display GPT-4o's response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)