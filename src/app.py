from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine
from .config import MONGO_SETTINGS


def create_app(is_testing=False):
    """
    Create the Flask app
    """
    app = Flask(__name__)

    app.config["MONGODB_SETTINGS"] = MONGO_SETTINGS

    api = Api(app)

    db = MongoEngine(app)

    return app, api, db
