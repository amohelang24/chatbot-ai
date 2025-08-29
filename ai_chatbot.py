import datetime
import requests
from config import Config

try:
    import ollama
    OLLAMA_PY_AVAILABLE = True
except ImportError:
    OLLAMA_PY_AVAILABLE = False

def append_log(role: str, content: str):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(Config.LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] {role.upper()}: {content}\n")

def ai_reply(messages):
    if OLLAMA_PY_AVAILABLE:
        resp = ollama.chat(
            model=Config.OLLAMA_MODEL,
            messages=messages,
            options={"temperature": Config.TEMPERATURE}
        )
        return resp["message"]["content"].strip()

    url = Config.OLLAMA_HOST + "/api/chat"
    payload = {"model": Config.OLLAMA_MODEL, "messages": messages}
    r = requests.post(url, json=payload, timeout=30)
    r.raise_for_status()
    return r.json()["message"]["content"].strip()

def main():
    messages = [{"role": "system", "content": Config.SYSTEM_PROMPT}]
    print(f"{Config.BOT_NAME} is ready! Type 'bye' to quit.\n")

    while True:
        user = input("You: ")
        if user.lower() in {"bye", "exit", "quit"}:
            print("AI: Goodbye 👋")
            break

        append_log("user", user)
        messages.append({"role": "user", "content": user})

        reply = ai_reply(messages)
        messages.append({"role": "assistant", "content": reply})
        append_log("assistant", reply)

        print("AI:", reply)

if __name__ == "__main__":
    main()
