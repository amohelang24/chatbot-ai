🤖 AmoBot — AI Chatbot

A simple AI-powered chatbot built in Python using the transformers
 library.
This project is my first GitHub project and is part of my journey to learn how to build and deploy AI applications.

✨ Features

Interactive chatbot interface in the terminal

Powered by LLaMA-2-7B (via Hugging Face transformers)

Customizable settings via config.json

Lightweight setup with a requirements file

Beginner-friendly and well-documented

📂 Project Structure
chatbot-ai/
│── ai_chatbot.py       # Main chatbot script
│── config.json         # Customization (bot name, model, greeting)
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation
│── .gitignore          # Ignore venv & cache files

🚀 Getting Started
1. Clone the repository
git clone https://github.com/amohelang24/chatbot-ai.git
cd chatbot-ai

2. Create & activate virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run the chatbot
python ai_chatbot.py

⚙️ Customization

Edit config.json to quickly change:

Bot name

Model name

Greeting message

Example:

{
  "bot_name": "AmoBot",
  "model": "meta-llama/Llama-2-7b-chat-hf",
  "greeting": "Hello! I’m your friendly chatbot 🤖"
}

🛠️ Tech Stack

Python 3.9+

Hugging Face Transformers

LLaMA-2 (open-source language model)

📚 Learning Goals

Understand basics of Python for AI

Learn how to structure and publish a project on GitHub

Build a foundation for future chatbot projects (e.g., with OCI, cloud deployment, web UI)

📝 License

This project is open-source and available under the MIT License
.