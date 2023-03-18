from bs4 import BeautifulSoup, SoupStrainer
from grequests import get, map


def scrape_page(page):
    ids = []
    soup = BeautifulSoup(page.text, "lxml")
    for i in soup.find_all(
        "div",
        {
            "class": "eds-event-card-content__actions-container eds-event-card-content__actions-container--consumer eds-event-card-content__actions-container--always-visible"
        },
    ):
        ids.append(i.find("span")["class"][0][28:40])
    return dict(enumerate(ids))


def get_data():
    fin = {}
    rs = (
        get(f"https://www.eventbrite.com/d/ca--santa-cruz/all-events/?page={i}")
        for i in range(1, 6)
    )
    stack = map(rs)
    fin = {}
    for i, j in enumerate(stack):
        fin[i + 1] = scrape_page(j)
    return fin
