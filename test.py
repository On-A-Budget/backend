import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.eventbrite.com/d/ca--santa-cruz/all-events/?page=1")


soup = BeautifulSoup(resp.text, "lxml")

with open("test.html", "w") as f:
    f.write(str(soup))

for i in soup.find_all(
    "div",
    {
        "class": "eds-event-card-content__sub eds-text-bm eds-text-color--ui-600 eds-l-mar-top-1"
    },
):
    print(i.text)
    print(i.name)

gfg = soup.find_all(lambda tag: tag.name == "div" and "$" in tag.text)

print(gfg)
