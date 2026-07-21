"""
storage.py
KC Notifier v2.0
Stores the last notified notice in a GitHub Issue.
"""

import requests

from config import (
    GITHUB_TOKEN,
    GITHUB_REPOSITORY
)

ISSUE_TITLE = "KC_NOTIFIER_STATE"


def github_headers():
    return {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }


def get_issue():
    """
    Returns the state issue if it exists.
    """

    url = f"https://api.github.com/repos/{GITHUB_REPOSITORY}/issues"

    r = requests.get(
        url,
        headers=github_headers(),
        timeout=30
    )

    r.raise_for_status()

    issues = r.json()

    for issue in issues:

        if issue["title"] == ISSUE_TITLE:
            return issue

    return None


def create_issue():
    """
    Creates the storage issue.
    """

    url = f"https://api.github.com/repos/{GITHUB_REPOSITORY}/issues"

    payload = {
        "title": ISSUE_TITLE,
        "body": ""
    }

    r = requests.post(
        url,
        headers=github_headers(),
        json=payload,
        timeout=30
    )

    r.raise_for_status()

    return r.json()


def read_state():
    """
    Reads the last notice ID.
    """

    issue = get_issue()

    if issue is None:
        issue = create_issue()

    return issue["body"].strip()


def write_state(value):
    """
    Updates the stored notice ID.
    """

    issue = get_issue()

    if issue is None:
        issue = create_issue()

    issue_number = issue["number"]

    url = (
        f"https://api.github.com/repos/"
        f"{GITHUB_REPOSITORY}/issues/{issue_number}"
    )

    payload = {
        "body": value
    }

    r = requests.patch(
        url,
        headers=github_headers(),
        json=payload,
        timeout=30
    )

    r.raise_for_status()

    return True
