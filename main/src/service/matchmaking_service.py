from discord import Interaction

from database.system.user_form import user_system
from templates.embeds.user_profile import UserProfileEmbed
from templates.view_builder.dating_view_builder import DatingMenuView


# todo - доробити пошук партнерів тут
class MatchmakingService:
    def __init__(self, client):
        self.client = client
        self.reset_variables()

        self.function_map = {
            'find_person': self.find_person,
        }
        self.function_called = {}

    def reset_variables(self):
        """
        This function resets the class variables to their default values.
        """

    async def call_function(self, interaction: Interaction, function_name: str):
        """
        # This function calls the function with the given name, if it exists.

        # Args:
          # The interaction that triggered the function.
          interaction: Interaction
          # The name of the function to call.
          function_name: str
        """
        if function_name in self.function_map:
            if function_name in self.function_called and self.function_called[function_name]:
                return False

            self.function_called[function_name] = True
            return await self.function_map[function_name](interaction)

    async def find_person(self, interaction: Interaction):
        dating_view = DatingMenuView(None, None, None, None, None, None)
        fetch_user = user_system.fetch_variables_by_user(user=interaction.user)
        return await interaction.response.send_message(embed=UserProfileEmbed(fetch_user).embed, view=dating_view)
