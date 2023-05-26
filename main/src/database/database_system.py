from pymongo import MongoClient
from config import MONGO_URL


class DatabaseSystem(object):
    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self._db = self.client.Cupidon

    @property
    def db(self):
        return self._db

    @property
    def user_collection(self):
        return self._db.user_collection
