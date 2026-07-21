🎓 Karimganj College Notice Notifier

Automatically monitors the Karimganj College Notice Board and sends a Telegram notification whenever a new notice is published.

Features

- ✅ Checks the notice board every 30 minutes
- ✅ Sends instant Telegram notifications
- ✅ Runs automatically using GitHub Actions
- ✅ Completely free
- ✅ No server required
- ✅ Easy to maintain

---

Project Structure

college-notifier/
│
├── check.py
├── requirements.txt
├── last_notice.txt
├── README.md
└── .github/
    └── workflows/
        └── checker.yml

---

Requirements

- GitHub Account
- Telegram Account
- Telegram Bot
- Bot Token
- Chat ID

---

Create Telegram Bot

1. Open Telegram.
2. Search BotFather.
3. Send:

/newbot

4. Follow the instructions.
5. Copy the Bot Token.

---

Get Chat ID

Search Telegram for userinfobot.

Start the bot.

Copy your Chat ID.

---

Create GitHub Repository

Create a repository named:

college-notifier

Upload all project files.

---

Add GitHub Secrets

Open:

Settings

↓

Secrets and variables

↓

Actions

Create:

BOT_TOKEN

Value:

Your Telegram Bot Token

Create:

CHAT_ID

Value:

Your Chat ID

---

Enable Workflow Permissions

Repository Settings

↓

Actions

↓

General

↓

Workflow Permissions

Select:

Read and write permissions

Click Save.

---

Run for the First Time

Open:

Actions

↓

Karimganj College Notice Checker

↓

Run workflow

The script will check the website and save the latest notice.

---

Automatic Checking

GitHub Actions runs automatically every 30 minutes.

When a new notice is detected, a Telegram message is sent automatically.

---

Example Notification

📢 Karimganj College New Notice

FYUG Merit List

https://www.karimganjcollege.ac.in/notice-board.aspx

---

Updating

Simply push changes to GitHub.

GitHub Actions automatically uses the latest version.

---

Troubleshooting

BOT_TOKEN missing

Check GitHub Secrets.

---

CHAT_ID missing

Verify the Chat ID secret.

---

Telegram notification not received

- Confirm the bot token is correct.
- Start a chat with your bot on Telegram.
- Send "/start" to the bot.

---

GitHub Action failed

Open:

Actions

↓

Latest Run

↓

View Logs

Read the error message.

---

License

Free to use for educational purposes.
