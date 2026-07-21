import json
import os

STATE_FILE = "last_notice.json"


def load_state():
    if not os.path.exists(STATE_FILE):
        return {"last_notice": ""}

    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"last_notice": ""}


def save_state(value):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(
            {"last_notice": value},
            f,
            indent=4
        )


def get_last_notice():
    return load_state().get("last_notice", "")


def set_last_notice(value):
    save_state(value)
