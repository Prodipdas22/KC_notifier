"""
check.py
KC Notifier v2.1
"""

from config import validate
from scraper import fetch_notices
from telegram import send_notice
from storage import get_last_notice, set_last_notice


def build_notice_id(notice):
    """
    Create a unique ID for a notice.
    """
    return f"{notice['date']}|{notice['title']}"


def main():

    print("=" * 50)
    print("KC NOTIFIER V2.1")
    print("=" * 50)

    validate()

    print("Loading notices...")

    notices = fetch_notices()

    if not notices:
        print("No notices found.")
        return

    print(f"Found {len(notices)} notices.")

    last_notice = get_last_notice()

    print("Last stored notice:")
    print(last_notice)

    latest_id = build_notice_id(notices[0])

    # First run
    if last_notice == "":
        print("First run detected.")

        set_last_notice(latest_id)

        print("State initialized.")
        return

    if latest_id == last_notice:
        print("No new notice.")
        return

    print("Searching for new notices...")

    new_notices = []

    for notice in notices:

        notice_id = build_notice_id(notice)

        if notice_id == last_notice:
            break

        new_notices.append(notice)

    if not new_notices:
        print("Nothing new.")
        return

    print(f"New notices found: {len(new_notices)}")

    # Send oldest first
    new_notices.reverse()

    for notice in new_notices:

        print("Sending:")
        print(notice["title"])

        send_notice(
            notice["title"],
            notice["link"]
        )

    set_last_notice(latest_id)

    print("Database updated.")
    print("Done.")


if __name__ == "__main__":

    try:
        main()

    except Exception as e:
        print("ERROR:", e)
        raise
