from flask import Flask
from flask import request
from flask_restful import Api
from flask_mongoengine import MongoEngine
from .config import MONGO_SETTINGS
from .model.item import Item
from .resources.items import Items

def create_app():
    """
    Create the Flask app
    """
    app = Flask(__name__)

    app.config["MONGODB_SETTINGS"] = MONGO_SETTINGS

    api = Api(app)

    api.add_resource(Items, "/items", "/items/<string:name>")

    db = MongoEngine(app)

    return app, api, db
