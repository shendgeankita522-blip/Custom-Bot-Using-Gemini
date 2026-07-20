# 🤖 Gemini Chatbot using Streamlit

A Generative AI chatbot built using **Google Gemini API** and **Streamlit**.  
This project allows users to interact with Google's Gemini AI model through a simple and interactive web application.

## 🚀 Features

- Chat with Google Gemini AI
- Real-time AI-generated responses
- Interactive chatbot interface using Streamlit
- Secure API key management using `.env`
- Simple Generative AI application

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- python-dotenv

## 📂 Project Structure

```
Custom-Bot-Using-Gemini/
│
├── gemini-app.py
├── main.py
├── textgemini.py
├── checks-models.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### Clone Repository

```bash
git clone your-github-repository-url
```

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Add Gemini API Key

Create a `.env` file in the project folder:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

### Run Application

```bash
python -m streamlit run gemini-app.py
```

## 💻 Demo Output

### User Input

```
What is Generative AI?
```

### Gemini Response

```
Generative AI is a branch of artificial intelligence
that can create new content such as text, images,
code, and other data by learning patterns from
existing information.
```

## 🖥️ Application Preview

Add your Streamlit chatbot screenshot here:

![Gemini Chatbot Demo](output/demo.png.png)

## 🔐 Security

- API keys are stored securely in `.env` file.
- `.env` file is added to `.gitignore`.
- Sensitive credentials are not uploaded to GitHub.

## 🔮 Future Improvements

- Add chat history
- Add conversation memory
- Add voice input and output
- Add LangSmith monitoring
- Deploy application on cloud platforms

## 👩‍💻 Author

**Ankita Shendge**
