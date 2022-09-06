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
            return [item.to_json() for item in Item.objects], requests.codes.ok

        item, json_msg = Item.get_by_name(name)

        return self.__create_response(item, json_msg, requests.codes.ok)

    def post(self):
        data = request.get_json(force=True)

        try:
            item = Item(
                name=data.get("name", None),
                weight=data["weight"],
                value=data["value"],
                imageUrl=data["imageUrl"],
            )

            item.save()
        except me.errors.NotUniqueError:
            return simple_error_response(
                DUPLICATED_ITEM_MSG, requests.codes.unprocessable_entity
            )

        return item.to_json(), requests.codes.created

    def patch(self, name):
        item, json_msg = Item.get_by_name(name)

        item_data = request.get_json(force=True)

        item.update(**item_data)

        item.reload()

        return self.__create_response(item, json_msg, requests.codes.ok)

    def delete(self, name):
        item, json_msg = Item.get_by_name(name)

        if item is None:
            return self.__create_response(item, json_msg, requests.codes.not_found)

        Item.delete(item)

    def __create_response(self, item, json_msg, response_code):
        if item is None:
            return simple_error_response(json_msg, response_code)

        return item.to_json(), response_code
