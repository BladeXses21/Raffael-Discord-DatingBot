from pymongo import MongoClient
from config import MONGO_URL


class DatabaseSystem(object):
    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self._db = self.client.Raffael

    @property
    def db(self):
        return self._db

    @property
    def user_form_collect(self):
        return self._db.user_form

    @property
    def user_confirmation_collect(self):
        return self._db.user_confirmation

    @property
    def user_profile_collect(self):
        return self._db.user_profile_collect
