from flask import Flask, request
import requests
import os

app = Flask(__name__)

# A bot token a környezeti változóból jön (Render-en be kell állítani!)
TOKEN = os.environ.get("TOKEN")

@app.route("/")
def home():
    return "Bot is live!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("🔔 ÉRKEZETT ÜZENET:", data)

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        reply = f"Te azt írtad: {text}"

        send_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": reply
        }

        r = requests.post(send_url, json=payload)
        print("✅ Válaszküldés:", r.status_code)

    return "ok"
