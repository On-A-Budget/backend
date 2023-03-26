import os


class Config:
    JSON_SORT_KEYS = False
    EVENTBRITE_TOKEN = os.environ.get("EVENTBRITE_TOKEN")
