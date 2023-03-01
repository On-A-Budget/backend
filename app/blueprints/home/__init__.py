from flask import Blueprint

from app import app

home = Blueprint("home", __name__)

@home.route("/")
def index():
    return "Hello, World!"
