import os
import requests
from dotenv import load_dotenv

load_dotenv()

class Webhooks:
    @staticmethod
    def send_to_telegram(message):
        TOKEN = os.getenv("TELEGRAM_TOKEN")
        CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
        URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

        obj = {
            "text": message,
            "chat_id": CHAT_ID
        }

        response = requests.post(URL, json=obj)
        return response