# AmoBot 🤖

A lightweight, customizable AI chatbot powered by [Ollama](https://ollama.ai/) running locally.  
Built in Python with support for environment configs, memory, and chat logging.

---

## 🚀 Features
- Runs fully **offline** with Ollama models (default: `phi3:mini`)
- Easy customization via `.env` file
- Chat history logging
- Configurable memory (remembers last few turns)
- Simple, clean codebase for hacking

---

## ⚡ Quickstart

### 1. Install Ollama
Download and install from: [https://ollama.ai/download](https://ollama.ai/download)  
Pull a model (example):
```bash
ollama pull phi3:mini
