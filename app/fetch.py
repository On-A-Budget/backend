from datetime import datetime

import requests
from bs4 import BeautifulSoup
from grequests import get, map

from app import eb_auth


def scrape_ids(page):
    ids = []
    soup = BeautifulSoup(page.text, "lxml")
    for i in soup.find_all(
        "div",
        {
            "class": "eds-event-card-content__actions-container eds-event-card-content__actions-container--consumer eds-event-card-content__actions-container--always-visible"
        },
    ):
        ids.append(i.find("span")["class"][0][28:40])
    full = dict.fromkeys(ids)
    resp = requests.get(
        f"https://www.eventbrite.com/api/v3/destination/events/?event_ids={','.join(ids)}&expand=ticket_availability,image&page_size={len(ids)}"
    ).json()
    for i in resp["events"]:
        pr = (
            f"${i['ticket_availability']['minimum_ticket_price']['major_value']}"
            if i["ticket_availability"]["minimum_ticket_price"]
            else None
        )
        full[i["id"]] = {
            "name": i["name"],
            "date": " ".join(
                datetime.strptime(i["end_date"], "%Y-%m-%d").strftime("%b %e").split()
            ),
            "price": pr if pr != "$0.00" else None,
            "image": i.get("image", {}).get("url"),
        }
    return full


def get_ids(p=5):
    fin = {}
    rs = (
        get(f"https://www.eventbrite.com/d/ca--santa-cruz/all-events/?page={i}")
        for i in range(1, p)
    )
    stack = map(rs)
    for i in stack:
        fin |= scrape_ids(i)
    return fin
