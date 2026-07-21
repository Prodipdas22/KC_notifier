"""
scraper.py
KC Notifier v2.0
"""

import requests
from bs4 import BeautifulSoup
from config import NOTICE_URL, HEADERS, REQUEST_TIMEOUT


def fetch_notices():
    """
    Returns a list of notices.

    Each notice is a dictionary:
    {
        "date": "...",
        "title": "...",
        "link": "..."
    }
    """

    response = requests.get(
        NOTICE_URL,
        headers=HEADERS,
        timeout=REQUEST_TIMEOUT
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

    for row in rows[1:]:

        cols = row.find_all("td")

        if len(cols) < 3:
            continue

        date = cols[0].get_text(strip=True)

        title = cols[1].get_text(" ", strip=True)

        link_tag = cols[2].find("a")

        link = ""

        if link_tag:
            link = link_tag.get("href", "").strip()

        notices.append(
            {
                "date": date,
                "title": title,
                "link": link
            }
        )

    return notices


def latest_notice():

    notices = fetch_notices()

    if not notices:
        raise Exception("No notices found.")

    return notices[0]


if __name__ == "__main__":

    data = fetch_notices()

    print(f"Found {len(data)} notices\n")

    for notice in data:

        print("--------------------------")
        print("Date :", notice["date"])
        print("Title:", notice["title"])
        print("Link :", notice["link"])
