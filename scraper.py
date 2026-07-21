"""
scraper.py
KC Notifier v2.1
"""

from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from config import (
    NOTICE_URL,
    HEADERS,
    REQUEST_TIMEOUT,
)


def fetch_notices():
    """
    Scrape all notices.

    Returns:
        [
            {
                "date": "...",
                "title": "...",
                "link": "..."
            }
        ]
    """

    response = requests.get(
        NOTICE_URL,
        headers=HEADERS,
        timeout=REQUEST_TIMEOUT,
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    table = soup.find(
        "table",
        id="ctl00_ContentPlaceHolder1_GridView1"
    )

    if table is None:
        raise Exception("Notice table not found.")

    notices = []

    rows = table.find_all("tr")

    # Skip header row
    for row in rows[1:]:

        cols = row.find_all("td")

        if len(cols) < 3:
            continue

        date = cols[0].get_text(" ", strip=True)

        title = cols[1].get_text(" ", strip=True)

        link = ""

        anchor = cols[2].find("a", href=True)

        if anchor:

            href = anchor["href"].strip()

            link = urljoin(
                NOTICE_URL,
                href
            )

        if not title:
            continue

        notices.append({
            "date": date,
            "title": title,
            "link": link
        })

    return notices


def latest_notice():

    notices = fetch_notices()

    if not notices:
        raise Exception("No notices found.")

    return notices[0]


if __name__ == "__main__":

    notices = fetch_notices()

    print("=" * 60)
    print("KC NOTIFIER SCRAPER TEST")
    print("=" * 60)

    print(f"Found {len(notices)} notices.\n")

    for i, notice in enumerate(notices, start=1):

        print(f"Notice {i}")

        print("Date :", notice["date"])
        print("Title:", notice["title"])
        print("Link :", notice["link"])

        print("-" * 60)
