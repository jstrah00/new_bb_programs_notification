import requests
from os import getenv
from logger import get_logger


TOKEN = getenv("BOT_TOKEN")
CHAT_ID = getenv("PERSONAL_CHAT_ID")
logger = get_logger(__name__)


def send_telegram_message(message):
    logger.debug("Sending telegram message")
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, data=data)
    logger.debug(f"Send telegram message status code: {response.status_code}")
    return response.json()

def send_new_program_message(program):
    message = f"🚨*New program found!*🚨\n\n*Program:* {program['program']}\n*Type:* {program['type']}\n*Platform:* {program['platform']}\n*URL:* {program['url']}"
    send_telegram_message(message)
