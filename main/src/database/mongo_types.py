from mongoengine import *

connect("Cupidon")


class UserForm(Document):
    user_id = IntField(required=True, min_length=0)  # discord id
    user_age = IntField(min_value=0)
    user_gender = StringField(min_length=1)
    user_like_gender = StringField(min_length=1)
    user_location = StringField(min_length=1)
    user_games = StringField(min_length=0)
    user_description = StringField(min_length=0)
    user_photo = StringField(min_length=1)

