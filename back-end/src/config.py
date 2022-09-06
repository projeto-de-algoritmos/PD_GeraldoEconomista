import os

MONGO_SETTINGS = {
    "host": "knapsack-db",
    "port": 27017,
    "db": os.getenv("DB_NAME", "knapsack"),
    "username": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "example"),
}
