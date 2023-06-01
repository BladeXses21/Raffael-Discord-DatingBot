from database.database_system import DatabaseSystem
from database.mongo_types import UserForm
from model.user_model.user import UserModel


class UserSystem(DatabaseSystem):

    def create_user_form(self, user_id: int, age: int, gender: str, like_gender: str, location: str, games: str, description: str, photo: str):
        user_model = UserModel(id=user_id, age=age, gender=gender, like_gender=like_gender, location=location, games=games, description=description,
                               photo=photo)
        user_form = UserForm()
        user_form.user_id = user_model.id
        user_form.user_age = user_model.age
        user_form.user_gender = user_model.gender
        user_form.user_like_gender = user_model.like_gender
        user_form.user_location = user_model.location
        user_form.user_games = user_model.games
        user_form.user_description = user_model.description
        user_form.user_photo = user_model.photo
        self.user_collection.insert_one(user_form.to_mongo())


user_system = UserSystem()
