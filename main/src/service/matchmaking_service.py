from discord import Interaction

from model.user_model.user import UserForm
from templates.embeds.userProfile import UserProfileEmbed
from templates.view_builder.dating_view_builder import DatingMenuView


# todo - доробити пошук партнерів тут
class MatchmakingService:
    def __init__(self, client):
        self.like_user_profile = bool()
        self.block_user_profile = bool()
        self.skip_user_profile = bool()
        self.report_user_profile = bool()
        self.stop_search_user_profile = bool()
        self.approve_user_profile = bool()
        self.client = client

        self.function_map = {
            'find_user_profile': self.find_user_profile,
            'like_user': self.like_user,
            'block_user': self.block_user,
            'skip_user': self.skip_user,
            'report_user': self.report_user,
            'stop_search': self.stop_search,
            'approve_user': self.approve_user,

            # functions outside the class
            'like_user_profile': self.like_user_profile,
            'block_user_profile': self.block_user_profile,
            'skip_user_profile': self.skip_user_profile,
            'report_user_profile': self.report_user_profile,
            'stop_search_user_profile': self.stop_search_user_profile,
            'approve_user_profile': self.approve_user_profile
        }
        self.function_called = {}

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

    async def find_user_profile(self, interaction: Interaction = None, user_data: UserForm = None):

        user_language = 'en'
        if interaction is not None:
            user_language = interaction.locale

        async def like_user_profile(interact: Interaction):
            pass

        async def block_user_profile(interact: Interaction):
            pass

        async def skip_user_profile(interact: Interaction):
            pass

        async def report_user_profile(interact: Interaction):
            pass

        async def stop_search_user_profile(interact: Interaction):
            pass

        async def approve_user_profile(interact: Interaction):
            pass

        dating_view = DatingMenuView(like_user_profile, block_user_profile, skip_user_profile,
                                     report_user_profile, stop_search_user_profile, approve_user_profile)

        if user_data is not None:
            return await interaction.user.send(embed=UserProfileEmbed(user_data).embed)

        return await interaction.response.send_message(embed=UserProfileEmbed(user_data).embed, view=dating_view)

    async def like_user(self, interaction: Interaction):
        pass

    async def block_user(self, interaction: Interaction):
        pass

    async def skip_user(self, interaction: Interaction):
        pass

    async def report_user(self, interaction: Interaction):
        pass

    async def stop_search(self, interaction: Interaction):
        pass

    async def approve_user(self, interaction: Interaction):
        pass
