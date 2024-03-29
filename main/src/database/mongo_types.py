from mongoengine import connect, Document, IntField, StringField, BooleanField, fields

connect("Raffael")


class UserFormDB(Document):
    user_id = IntField(required=True)
    language = StringField(required=True)
    name = StringField(required=True)
    age = IntField(required=True)
    gender = StringField(required=True)
    opposite_gender = StringField(required=True)
    location = fields.ListField()
    games = StringField(required=True)
    description = StringField(required=True)
    photo = StringField(required=True)
    likes = IntField(default=0)


class UserConfirmationDB(Document):
    user_id = IntField(required=True)
    confirmed = BooleanField()
