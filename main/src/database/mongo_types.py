from mongoengine import connect, Document, IntField, StringField

connect("Raffael")


class UserForm(Document):
    user_id = IntField(required=True, min_length=1)  # discord id
    user_name = StringField(min_length=1)
    user_age = IntField(min_value=1)
    user_gender = StringField(min_length=1)
    user_like_gender = StringField(min_length=1)
    user_location = StringField(min_length=1)
    user_games = StringField(min_length=1)
    user_description = StringField(min_length=1)
    user_photo = StringField(min_length=1)
    user_language = StringField(min_length=1)
    user_likes = IntField(min_value=0)
