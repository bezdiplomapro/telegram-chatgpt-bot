import openai
import requests
from flask import Flask, request

app = Flask(__name__)


import os
openai.api_key = os.getenv("OPENAI_API_KEY")


TELEGRAM_TOKEN = "7635370036:AAEeZC2HReNw7P2H9xNeaI3F0qZr1uB161o"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    chat_id = data["message"]["chat"]["id"]
    user_text = data["message"]["text"]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_text}]
    )

    reply = response.choices[0].message.content.strip()

    requests.post(TELEGRAM_API_URL, json={
        "chat_id": chat_id,
        "text": reply
    })

    return "ok"
