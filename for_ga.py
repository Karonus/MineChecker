import os

import requests

import checker

NICKNAMES = os.environ.get("NICKNAMES")
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

if not all({NICKNAMES, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID}):
    raise RuntimeError(
        "You need to set NICKNAMES, "
        "TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID "
        "environment variables"
    )

for nickname in NICKNAMES.split(","):
    if checker.check(nickname):
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": f"<code>{nickname}</code> is available now!",
            "parse_mode": "HTML",
        }
        requests.post(url, json=data)
