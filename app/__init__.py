import json

import gevent.monkey

# fix ssl inf recursion error
gevent.monkey.patch_all()

from eventbrite import Eventbrite
from flask import Flask
from flask_cors import CORS

from config import Config


def create_app():
    print("init app...", end="", flush=True)
    app = Flask(__name__)
    app.config.from_object(Config)
    print("done")
    return app


app = create_app()


def register_blueprints(app):
    print("register blueprints...", end="", flush=True)
    from .blueprints.home import home

    app.register_blueprint(home)
    print("done")


def setup_firebase(app):
    print("auth with firestore...", end="", flush=True)
    # firebase stuff
    print("done")


with app.app_context():
    print("add extensions...", end="", flush=True)
    CORS(app)
    print("done")
    setup_firebase(app)

    print("fetch event ids...", end="", flush=True)
    from app.fetch import get_ids

    data = get_ids()
    with open("data.json", "w") as f:
        json.dump(data, f)
    print("done")

    print("auth eventbrite...", end="", flush=True)
    eb_auth = Eventbrite(app.config["EVENTBRITE_TOKEN"])
    print("done")

    register_blueprints(app)
