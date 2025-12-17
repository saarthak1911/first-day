import streamlit as st
from groq import groq_chat
from local import local_chat

st.title("Chatbot")

# Sidebar
with st.sidebar:
    st.header("Settings")
    mode = st.selectbox("Select Mode", ["GROQ", "Local LLM"])

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat input
user_msg = st.chat_input("Say something...")

if user_msg:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_msg})

    # Get response
    if mode == "GROQ":
        st.write("Using GROQ API...")
        response_text = groq_chat(user_msg)
    else:
        st.write("Using Local LLM...")
        response_text = local_chat(user_msg)

    # Store assistant response
    st.session_state.messages.append({"role": "assistant", "content": response_text})

# Display chat history (question followed by answer)
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])
