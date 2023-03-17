from bs4 import BeautifulSoup, SoupStrainer
from flask import Blueprint
from httpx import get

from app import app

home = Blueprint("home", __name__)


@home.route("/")
def index():
    return "Hello, World!"


@home.route("/ids")
def ids():
    ids = {}
    for i in range(1, 6):
        page = get(f"https://www.eventbrite.com/d/ca--santa-cruz/all-events/?page={i}")
        soup = BeautifulSoup(
            page.text,
            "lxml-xml",
            parse_only=SoupStrainer(
                "div",
                {
                    "class": "eds-event-card-content__actions-container eds-event-card-content__actions-container--consumer eds-event-card-content__actions-container--always-visible"
                },
            ),
        )
        for i, j in enumerate(soup):
            print(i, j)
            ids[i] = j.get("class")[28:40]
    return ids
