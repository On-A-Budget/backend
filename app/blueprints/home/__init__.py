import asyncio
import json

from bs4 import BeautifulSoup, SoupStrainer
from flask import Blueprint

from app import app

home = Blueprint("home", __name__)


@home.route("/")
def index():
    return "Hello, World!"


@home.route("/ids")
def ids():
    with open("data.json") as json_file:
        data = json.load(json_file)
    return data
