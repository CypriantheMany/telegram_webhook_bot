from flask import Flask, request
import requests

app = Flask(__name__)
TOKEN = "7353347441:AAE95EY3Jatrxa3KN_uWUrgJNKQFqSsi5Gk"

@app.route('/')
def index():
    return "Bot él"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        reply = f"Te ezt írtad: {text}"
        requests.post(f"https://api.telegram.org/bot{TO7353347441:AAE95EY3Jatrxa3KN_uWUrgJNKQFqSsi5GkKEN}/sendMessage", json={
            "chat_id": chat_id,
            "text": reply
        })
    return "ok"
