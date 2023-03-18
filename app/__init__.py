import json

from flask import Flask
from flask_cors import CORS

from config import Config

from .fetch import get_data


def create_app():
    print("starting app...", end="", flush=True)
    app = Flask(__name__)
    app.config.from_object(Config)
    print("done")
    return app


app = create_app()

print("defining helpers...", end="", flush=True)
# helper funcs go here


def register_blueprints(app):
    print("registering blueprints...", end="", flush=True)
    from .blueprints.home import home

    app.register_blueprint(home)
    print("done")


def setup_firebase(app):
    print("setting up firebase...", end="", flush=True)
    # firebase stuff
    print("done")


print("done")

with app.app_context():
    print("adding extensions...", end="", flush=True)
    CORS(
        app
    )  # allow js to send requests (https://flask-cors.readthedocs.io/en/latest/)
    print("done")
    setup_firebase(app)
    register_blueprints(app)
    from . import fetch

    data = get_data()
    with open("data.json", "w") as f:
        json.dump(data, f)
