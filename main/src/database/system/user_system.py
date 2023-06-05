from discord import User

from database.database_system import DatabaseSystem
from database.mongo_types import UserForm
from model.user_model.user import UserModel


class UserSystem(DatabaseSystem):

    def create_user_form(self, user_id: int, name: str, age: int, gender: str, like_gender: str, location: str, games: str, description: str, photo: str,
                         language: str):
        user_model = UserModel(user_id=user_id, name=name, age=age, gender=gender, like_gender=like_gender, location=location, games=games, description=description,
                               photo=photo, language=language)
        user_form = UserForm()
        user_form.user_id = user_model.user_id
        user_form.user_name = user_model.user_name
        user_form.user_age = user_model.user_age
        user_form.user_gender = user_model.user_gender
        user_form.user_like_gender = user_model.user_like_gender
        user_form.user_location = user_model.user_location
        user_form.user_games = user_model.user_games
        user_form.user_description = user_model.user_description
        user_form.user_photo = user_model.user_photo
        user_form.user_language = user_model.user_language
        user_form.user_likes = user_model.user_likes

        self.user_collection.insert_one(user_form.to_mongo())

    def fetch_variables_by_user(self, user: User):
        user_data = self.user_collection.find_one({"user_id": user.id}, {})
        if user_data is not None:
            return UserModel.parse_obj(user_data)

        return False


user_system = UserSystem()
