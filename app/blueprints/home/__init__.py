import asyncio
import json

from bs4 import BeautifulSoup, SoupStrainer
from flask import Blueprint

from app import app, eb_auth

home = Blueprint("home", __name__)


@home.route("/")
def index():
    return "Hello, World!"


@home.route("/events")
def events():
    with open("data.json") as f:
        data = json.load(f)
    return data


@home.route("/events/<int:id>")
def events_id(id: int):
    return eb_auth.get_event(str(id))
