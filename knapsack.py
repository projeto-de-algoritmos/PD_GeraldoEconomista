def knapSack(capacity, item_weight, items, n):
    memoization = [0 for _ in range(capacity + 1)]

    for i in range(1, n + 1):
        for w in range(capacity, 0, -1):
            if item_weight[i - 1] <= w:
                memoization[w] = max(memoization[w], memoization[w - item_weight[i - 1]] + items[i - 1])

    return memoization[capacity]  # returning the maximum value of knapsack


# teste
items = [60, 100, 120, 40, 20]
item_weight = [10, 20, 30, 5, 2]
capacity = 50
n = len(items)
print(knapSack(capacity, item_weight, items, n))
