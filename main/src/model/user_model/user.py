from pydantic import BaseModel

from enum import Enum, unique


@unique
class EnumUserGender(str, Enum):
    Man = 'Man'
    Woman = 'Woman'

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class User(BaseModel):
    user_id = int
    username = str
    city = str
    gender = str
    age = int
    interest = str

    def get_user_id(self):
        return self.user_id

    def get_username(self):
        return self.username

    def get_city(self):
        return self.city

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def get_interest(self):
        return self.interest
