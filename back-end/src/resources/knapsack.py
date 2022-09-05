import requests
import mongoengine as me
import json
from src.model.item import Item
from flask import request
from flask_restful import Resource
from src.resources.utils import simple_error_response

class Knapsack(Resource):

    def post(self):
        request_data = request.get_json(force=True)

        request_items = request_data['items']

        items = []

        for item in request_items:
            for i in range(0, item['quantity']):
                item_info, json_msg = Item.get_item(item['name'])

                if item_info is None:
                    return simple_error_response(json_msg, requests.codes.not_found)

                items.append(item_info)

        return self.__knapsack(request_data['capacity'], items, len(items))



    def __knapsack(self, knapsack_capacity, items, n):
        memoization = [0 for _ in range(knapsack_capacity + 1)]

        for i in range(1, n + 1):
            for w in range(knapsack_capacity, 0, -1):
                if items[i - 1].weight <= w:
                    memoization[w] = max(memoization[w], memoization[w - items[i - 1].weight] + items[i - 1].value)

        return memoization[knapsack_capacity]  # returning the maximum value of knapsack


# # teste
# # items = [60, 100, 120, 40, 20]
# # item = [10, 20, 30, 5, 2]
# items = []
# items.append(Item(name = "panela", weight = 10, value = 60))
# items.append(Item(name = "colher", weight = 20, value = 100))
# items.append(Item(name = "garfo", weight = 30, value = 120))

# print(items[0].weight)

# knapsack_capacity = 50
# n = len(items)
# print(knapsack(knapsack_capacity, items, n))
