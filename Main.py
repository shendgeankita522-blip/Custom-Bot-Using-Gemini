from dotenv import load_dotenv
import os
import google.generativeai as genai


load_dotenv()

google_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=google_key)


model = genai.GenerativeModel("gemini-3.5-flash")


question = input("Ask Gemini: ")

response = model.generate_content(question)

print(response.text)