import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

google_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=google_key)

for model in genai.list_models():
    print(model.name)