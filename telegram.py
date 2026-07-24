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


def send_message(text, notice_url = None, disable_preview=True):
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

    if notice_url:
        payload["reply_markup"] = json.dumps({
            "inline_keyboard": [
                [
                    {
                        "text": "📄 Open Notice",
                        "url": notice_url
                    }
                ]
            ]
        })

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
🔔 <b>KARIMGANJ COLLEGE NOTICE</b>

<b>{notice_type}</b>

📄 <code>{title}</code>

📅 <code>Published: {date}</code>


━━━━━━━━━━━━━━━━━━

🤖 <b>KC Notifier</b>
📍 <i>Karimganj College</i>
"""


def send_notice(title, date, link):
    """
    Send a formatted notice.
    """

    message = format_notice(title, date, link)

    return send_message(message,notice_url=link)


def send_test():
    """
    Send a test notification.
    """

    return send_message(
        "✅ <b>KC Notifier Test</b>\n\n"
        "Your Telegram bot is configured correctly."
    )
