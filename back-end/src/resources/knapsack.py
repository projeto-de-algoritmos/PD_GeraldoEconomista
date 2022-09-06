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

        request_items = request_data["items"]

        items = []

        for item in request_items:
            for i in range(0, item["quantity"]):
                item_info, json_msg = Item.get_by_name(item["name"])

                if item_info is None:
                    return simple_error_response(json_msg, requests.codes.not_found)

                items.append(item_info)

        return self.__knapsack(items, request_data["capacity"], len(items))

    def __knapsack(self, items, capacity, n):

        global memoization

        memoization = [[-1 for i in range(capacity + 1)] for j in range(n + 1)]

        result = self.__knapsack_calc(items, capacity, n)

        solution = self.__find_solution(items, capacity, n, result)

        total_weight = 0

        final_solution = []

        for item in solution:
            total_weight += item.weight
            final_solution.append(item.to_json())

        response = {
            "result": result,
            "weight": total_weight,
            "solution": final_solution,
        }

        return response, requests.codes

    def __knapsack_calc(self, items, capacity, n):
        global memoization

        if n == 0 or capacity == 0:
            return 0

        if memoization[n][capacity] != -1:
            return memoization[n][capacity]

        if items[n - 1].weight <= capacity:

            memoization[n][capacity] = max(
                float(items[n - 1].value)
                + self.__knapsack_calc(items, capacity - items[n - 1].weight, n - 1),
                self.__knapsack_calc(items, capacity, n - 1),
            )

            return memoization[n][capacity]

        elif items[n - 1].weight > capacity:

            memoization[n][capacity] = self.__knapsack_calc(items, capacity, n - 1)

            return memoization[n][capacity]

    def __find_solution(self, items, capacity, n, result):
        global memoization

        solution = []

        for i in range(n, 0, -1):

            if result <= 0:
                break

            if result == memoization[i - 1][capacity]:
                continue

            else:
                solution.append(items[i - 1])
                result -= float(items[i - 1].value)
                capacity -= items[i - 1].weight

        return solution


# # teste
# # items = [60, 100, 120, 40, 20]
# # item = [10, 20, 30, 5, 2]
# items = []
# items.append(Item(name = "panela", weight = 10, value = 60))
# items.append(Item(name = "colher", weight = 20, value = 100))
# items.append(Item(name = "garfo", weight = 30, value = 120))

# print(items[0].weight)

# capacity = 50
# n = len(items)
# print(knapsack(capacity, items, n))
