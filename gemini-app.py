import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os


# Load API key from .env
load_dotenv()

google_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=google_key)


# Create Gemini model
model = genai.GenerativeModel("gemini-3.5-flash")


# Streamlit UI
st.title("🤖 Gemini Chatbot")


user_input = st.text_input("Ask something:")


if user_input:
    response = model.generate_content(user_input)
    st.write(response.text)