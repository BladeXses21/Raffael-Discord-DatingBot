from discord import User

from database.database_system import DatabaseSystem
from database.mongo_types import UserConfirmationDB
from model.user_model.user import UserConfirmation


class UserConfirmed(DatabaseSystem):

    def user_confirm_rules(self, user: User) -> bool:
        """
        Confirmation of the rules for using the bot by the user.

        :param user:
            Args: user: discord.User
        :return:
            A boll
        """
        if self.user_confirmation_collect.find_one({"user_id": user.id}):
            return False
        user_confirmation_model = UserConfirmation(user_id=user.id, confirmed=True)
        user_confirmation_db = UserConfirmationDB()
        user_confirmation_db.user_id = user_confirmation_model.user_id
        user_confirmation_db.confirmed = user_confirmation_model.confirmed
        self.user_confirmation_collect.insert_one(user_confirmation_db.to_mongo())
        return True


user_confirmed = UserConfirmed()
