import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

google_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=google_key)

model = genai.GenerativeModel("gemini-3.5-flash")

response = model.generate_content(
    "Explain Generative AI in simple words"
)

print(response.text)