"""
telegram.py
KC Notifier v2.0
Telegram notification module.
"""

import requests
from config import BOT_TOKEN, CHAT_ID
from scraper import get_notice_type
import json

API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_message(text, disable_preview=True):
    """
    Send a Telegram message.

    Returns:
        True if successful
        False otherwise
    """

    url = f"{API_URL}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": disable_preview
    }

    try:
        response = requests.post(
            url,
            data=payload,
            timeout=30
        )

        response.raise_for_status()

        result = response.json()

        if result.get("ok"):
            print("✅ Telegram notification sent.")
            return True

        print("❌ Telegram API Error:")
        print(result)

        return False

    except requests.exceptions.Timeout:
        print("❌ Telegram request timed out.")
        return False

    except requests.exceptions.ConnectionError:
        print("❌ Unable to connect to Telegram.")
        return False

    except Exception as e:
        print("❌ Telegram Error:", e)
        return False


def format_notice(title, date, link):
    notice_type = get_notice_type(title)

    return f"""
🔔 <b>NEW KARIMGANJ COLLEGE NOTICE</b>

{notice_type}

📄 <b>Title</b>
{title}

📅 <b>Published</b>
{date}

🔗 <a href="{link}">Open Notice</a>

━━━━━━━━━━━━━━━━━━

🤖 <b>KC Notifier</b>
📍 Karimganj College
"""


def send_notice(title, date, link):
    """
    Send a formatted notice.
    """

    message = format_notice(title, date, link)

    return send_message(message)


def send_test():
    """
    Send a test notification.
    """

    return send_message(
        "✅ <b>KC Notifier Test</b>\n\n"
        "Your Telegram bot is configured correctly."
    )
