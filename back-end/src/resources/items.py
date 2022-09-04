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

    def post(self):
        data = request.get_json(force=True)

        try:
            item = Item(
                name=data.get("name", None),
                weight=data["weight"],
                value=data["value"],
                quantity=data["quantity"],
            )

            item.save()
        except me.errors.NotUniqueError:
            return simple_error_response(
                DUPLICATED_ITEM_MSG, requests.codes.unprocessable_entity
            )

        return item.to_json(), requests.codes.created

    def __show(self, name):
        item, json_msg = self.get_item(name)

        if item is None:
            return simple_error_response(json_msg, requests.codes.not_found)

        return item.to_json(), requests.codes.ok

    def __get_item(self, name):
        item = Item.objects(name__exac=name)

        if item is None:
            return None, f"There is no items with name {name}"

        if item.quantity <= 0:
            return None, f"There aren't available items {name}"

        return item, None
