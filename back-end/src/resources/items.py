import requests
import mongoengine as me
from src.model.item import Item
from flask import request
from src.resources.utils import simple_error_response
from flask_restful import Resource

DUPLICATED_ITEM_MSG = "The Item name is already in use"

class Items(Resource):
    def get(self, name=None):
        if name is None:
            return [item.to_json() for item in Item.objects]

        item, json_msg = Item.get_item(item)

        return self.__create_get_response(item, json_msg)

    def post(self):
        data = request.get_json(force=True)

        try:
            item = Item(
                name=data.get("name", None),
                weight=data["weight"],
                value=data["value"],
                image_url=data["image_url"]
            )

            item.save()
        except me.errors.NotUniqueError:
            return simple_error_response(
                DUPLICATED_ITEM_MSG, requests.codes.unprocessable_entity
            )

        return item.to_json(), requests.codes.created

    def __create_get_response(self, item, json_msg):
        if item is None:
            return simple_error_response(json_msg, requests.codes.not_found)
