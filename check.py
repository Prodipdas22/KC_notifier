import os
import requests
from bs4 import BeautifulSoup

# ==========================
# CONFIG
# ==========================

NOTICE_URL = "https://www.karimganjcollege.ac.in/notice-board.aspx"

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

LAST_NOTICE_FILE = "last_notice.txt"

# ==========================
# TELEGRAM
# ==========================

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }

    response = requests.post(url, data=payload, timeout=20)

    if response.status_code != 200:
        print("Telegram Error:")
        print(response.text)

# ==========================
# FILE
# ==========================

def load_last_notice():
    if not os.path.exists(LAST_NOTICE_FILE):
        return ""

    with open(LAST_NOTICE_FILE, "r", encoding="utf-8") as f:
        return f.read().strip()

def save_last_notice(value):
    with open(LAST_NOTICE_FILE, "w", encoding="utf-8") as f:
        f.write(value)

# ==========================
# SCRAPER
# ==========================

def get_latest_notice():

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        NOTICE_URL,
        headers=headers,
        timeout=30
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    # Find first notice link
    for a in soup.find_all("a", href=True):

        title = a.get_text(" ", strip=True)

        if len(title) < 5:
            continue

        href = a["href"]

        if "notice" in href.lower() or href.endswith(".pdf"):

            if href.startswith("http"):
                link = href
            else:
                link = requests.compat.urljoin(NOTICE_URL, href)

            return title, link

    raise Exception("Unable to find notice.")

# ==========================
# MAIN
# ==========================

def main():

    if not BOT_TOKEN:
        raise Exception("BOT_TOKEN missing")

    if not CHAT_ID:
        raise Exception("CHAT_ID missing")

    title, link = get_latest_notice()

    latest = title + "|" + link

    previous = load_last_notice()

    if latest == previous:
        print("No new notice.")
        return

    '''message = (
        "📢 <b>Karimganj College New Notice</b>\n\n"
        f"<b>{title}</b>\n\n"
        f"🔗 {link}"
    )

    send_telegram(message)'''

    message = "✅ Test message from GitHub Actions"
    send_telegram(message)

    save_last_notice(latest)

    print("Notification sent.")

if __name__ == "__main__":
    try:
        main()

    except Exception as e:
        print("ERROR:", e)
