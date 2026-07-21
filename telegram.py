"""
telegram.py
KC Notifier v2.0
Telegram notification module.
"""

import requests
from config import BOT_TOKEN, CHAT_ID

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


def format_notice(title, link):
    """
    Format a notice for Telegram.
    """

    return f"""📢 <b>Karimganj College Notice</b>

<b>{title}</b>

🔗 {link}

━━━━━━━━━━━━━━━
📸 <a href="https://instagram.com/prodip_das_22/"><b>@prodip_das_22</b></a>
"""


def send_notice(title, link):
    """
    Send a formatted notice.
    """

    message = format_notice(title, link)

    return send_message(message)


def send_test():
    """
    Send a test notification.
    """

    return send_message(
        "✅ <b>KC Notifier Test</b>\n\n"
        "Your Telegram bot is configured correctly."
    )
