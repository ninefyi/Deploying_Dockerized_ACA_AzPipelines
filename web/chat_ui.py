import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Chat API endpoint
API_URL = f"http://localhost:{os.getenv('FLASK_APP_PORT', 8080)}/chat"

if "CODESPACE_NAME" in os.environ:
    API_URL = f"https://{os.environ['CODESPACE_NAME']}-8080.app.github.dev/chat"


# Streamlit configuration
st.set_page_config(page_title="Chat AI", layout="centered")

# Application title
st.title("Chat AI")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to send prompt to API


def send_prompt(prompt):
    try:
        response = requests.post(API_URL, json={"prompt": prompt})
        response.raise_for_status()
        return response.json().get("response", "Error: No response from the server.")
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"


# User input
with st.form(key="chat_form"):
    user_input = st.text_input("You:", "")
    submit_button = st.form_submit_button(label="Send")

# Handle user input
if submit_button and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    ai_response = send_prompt(user_input)
    st.session_state.messages.append(
        {"role": "assistant", "content": ai_response})

# Display chat messages
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    elif message["role"] == "assistant":
        st.markdown(f"**AI:** {message['content']}")
