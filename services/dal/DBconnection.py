import os
import time
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


class MongoConnector:
    def __init__(self):
        self.client = None
        self.db = None

    def get_connection(self):
        if self.client:
            try:
                self.client.admin.command("ping")
                return self.db
            except ConnectionFailure:
                self.client = None

        host = os.getenv("MONGO_HOST")
        port = int(os.getenv("MONGO_PORT"))
        user = os.getenv("MONGO_USER")
        password = os.getenv("MONGO_PASSWORD")
        database = os.getenv("MONGO_DATABASE")

        uri = f"mongodb://{host}:{port}/"
        if user and password:
            uri = f"mongodb://{user}:{password}@{host}:{port}/{database}?authSource=admin"

        for _ in range(10):
            try:
                self.client = MongoClient(uri, serverSelectionTimeoutMS=3000)
                self.client.admin.command("ping")  # בדיקת חיבור
                self.db = self.client[database]
                return self.db
            except ConnectionFailure:
                time.sleep(3)

        raise RuntimeError("Cannot connect to MongoDB after several retries")

    def close_connection(self):
        if self.client:
            self.client.close()
            self.client = None
            self.db = None

    def __del__(self):
        self.close_connection()
