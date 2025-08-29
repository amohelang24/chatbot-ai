import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_NAME = os.getenv("BOT_NAME", "AmoBot")
    SYSTEM_PROMPT = os.getenv(
        "SYSTEM_PROMPT",
        "You are a helpful, concise AI assistant."
    )
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "phi3:mini")
    OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.2"))
    MEMORY_TURNS = int(os.getenv("MEMORY_TURNS", "6"))
    LOG_FILE = os.getenv("LOG_FILE", "chat_history.txt")
