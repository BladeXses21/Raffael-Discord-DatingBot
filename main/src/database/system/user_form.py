import array

from discord import User

from database.database_system import DatabaseSystem
from database.mongo_types import UserFormDB
from model.user_model.user import UserForm
from typing import Literal


class UserSystem(DatabaseSystem):

    def create_user_form(self, id: int, name: str, age: int, gender: str, opposite_gender: str, location: array.ArrayType, games: str,
                         description: str,
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
            self.user_form_collect.update_one({"user_id": user_model.user_id}, {"$set": user_form.to_mongo()})
            return True
        self.user_form_collect.insert_one(user_form.to_mongo())
        return True

    def update_user_field(self, user_id: int, field_name: str, new_value) -> bool:
        if field_name in UserForm.__annotations__:
            if field_name == "age":
                update_query = {"$set": {field_name: int(new_value)}}
                self.user_form_collect.update_one({"user_id": user_id}, update_query)
            else:
                update_query = {"$set": {field_name: new_value}}
                result = self.user_form_collect.update_one({"user_id": user_id}, update_query)
            if result.matched_count > 0:
                return True
            else:
                return False
        else:
            return False

    def fetch_variables_by_user(self, user: User):
        user_data = self.user_form_collect.find_one({"user_id": user.id}, {})
        if user_data is None:
            return False
        return user_data

    def get_all_users(self) -> list[UserForm]:
        users_data = self.user_form_collect.find({})
        users = []
        for i in users_data:
            users.append(UserForm.parse_obj(i))
        return users


user_system = UserSystem()
