"""
config.py
KC Notifier v2.0
Central configuration file.
"""

import os

# ==============================
# Website Configuration
# ==============================

BASE_URL = "https://www.karimganjcollege.ac.in"
NOTICE_URL = f"{BASE_URL}/notice-board.aspx"

# ==============================
# Telegram Configuration
# ==============================

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
CHAT_ID = os.getenv("CHAT_ID", "").strip()

# ==============================
# GitHub Configuration
# ==============================

# GitHub automatically provides this token to Actions.
# No need to create it manually.
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "").strip()

# Repository name
# Example:
# Prodipdas22/KC_notifier
GITHUB_REPOSITORY = os.getenv("GITHUB_REPOSITORY", "").strip()

# ==============================
# HTTP Configuration
# ==============================

REQUEST_TIMEOUT = 60

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/138.0 Safari/537.36"
)

HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

# ==============================
# Notification Settings
# ==============================

MAX_NOTICES_PER_RUN = 10

SEND_PREVIEW = False

# ==============================
# Debug
# ==============================

DEBUG = True

# ==============================
# Validation
# ==============================

def validate():
    """
    Ensure required environment variables are available.
    """
    missing = []

    if not BOT_TOKEN:
        missing.append("BOT_TOKEN")

    if not CHAT_ID:
        missing.append("CHAT_ID")

    if missing:
        raise RuntimeError(
            "Missing environment variable(s): "
            + ", ".join(missing)
        )
