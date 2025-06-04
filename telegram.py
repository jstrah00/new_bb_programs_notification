import requests
from os import getenv
from logger import get_logger
from utils import escape_markdown


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
    logger.debug(f"Send telegram message response: {response.text}")
    return response.json()

def send_new_program_message(program):
    message = (
        f"🚨*New program found!*🚨\n\n"
        f"*Program:* {escape_markdown(program['program'])}\n"
        f"*Type:* {escape_markdown(program['type'])}\n"
        f"*Platform:* {escape_markdown(program['platform'])}\n"
        f"[Go to program]({program['url']})"
    )
    send_telegram_message(message)
