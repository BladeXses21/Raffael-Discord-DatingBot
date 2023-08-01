from discord import User

from database.database_system import DatabaseSystem
from database.mongo_types import UserFormDB
from model.user_model.user import UserForm


class UserSystem(DatabaseSystem):

    def create_user_form(self, id: int, name: str, age: int, gender: str, opposite_gender: str, location: str, games: str, description: str,
                         photo: str, language: str) -> bool:
        user_model = UserForm(user_id=id, name=name, age=age, gender=gender, opposite_gender=opposite_gender, location=location, games=games,
                              description=description, photo=photo, language=language)
        user_form = UserFormDB()
        user_form.user_id = user_model.user_id
        user_form.name = user_model.name
        user_form.age = user_model.age
        user_form.gender = user_model.gender
        user_form.opposite_gender = user_model.opposite_gender
        user_form.location = user_model.location
        user_form.games = user_model.games
        user_form.description = user_model.description
        user_form.photo = user_model.photo
        user_form.language = user_model.language
        user_form.likes = user_model.likes

        if self.user_form_collect.find_one({"user_id": user_model.user_id}, {}):
            self.user_form_collect.update_one({"user_id": user_model.user_id}, {"$set": {user_form.to_json()}})
            return True
        self.user_form_collect.insert_one(user_form.to_mongo())
        return True

    def fetch_variables_by_user(self, user: User):
        user_data = self.user_form_collect.find_one({"user_id": user.id}, {})
        if user_data is None:
            return False
        return user_data


user_system = UserSystem()
