import discord
from discord.ext import commands
from discord import Bot, Interaction

from cog.base import BaseCog
from database.system.user_form import user_system
from extension.logger import logger

from config import GUILD_IDS
from service.matchmaking_service import MatchmakingService
from service.private_message_service import PrivateMessageService
from templates.localization.translations import translate_text


class DefaultUser(BaseCog):
    def __init__(self, client: Bot):
        super().__init__(client)
        self.private_message_service = PrivateMessageService(client)
        self.matchmaking_service = MatchmakingService(client)
        self.start_command_cooldown = commands.CooldownMapping.from_cooldown(1, 15, commands.BucketType.user)
        logger.info("Cog DefaultUser connected")

    user = discord.SlashCommandGroup('user', 'default command for user', guild_ids=[*GUILD_IDS])

    @commands.Cog.listener()
    async def on_message(self, message):
        """ A function that monitors all user messages and, if it finds the desired message, will respond to it

        :param message: discord.Message
        :return:
            Return a discord.Embed from the file private_message_service.py depending on whether the user has been registered before
        """
        if message.content == "старт" or message.content == "start":
            retry_after = self.start_command_cooldown.get_bucket(message).update_rate_limit()
            if retry_after:
                return False
            user_data = user_system.fetch_variables_by_user(message.author)
            if user_data is not False:
                return await self.private_message_service.control_panel(interaction=None, user_data=user_data)
            return await self.private_message_service.language_scanning(message.author)
        pass

    @commands.Cog.listener()
    async def on_interaction(self, interaction: Interaction):
        user_language = interaction.locale
        if interaction.data['custom_id'] == 'start_dating':
            await self.private_message_service.presentation_one(interaction)
            return await interaction.response.send_message(content=translate_text('check_private_messages', user_language), ephemeral=True)
        if interaction.data['custom_id'] == 'create_form':
            return await self.private_message_service.user_name(interaction)
        if interaction.data['custom_id'] == 'look_form':
            return await self.private_message_service.user_profile(interaction)
        if interaction.data['custom_id'] == 'settings_form':
            return await self.private_message_service.user_settings(interaction)
        if interaction.data['custom_id'] == 'button_back':
            return await self.private_message_service.back_to_menu(interaction)
        if interaction.data['custom_id'] == 'button_photo':
            return await self.private_message_service.edit_photo(interaction)
        if interaction.data['custom_id'] == 'button_description':
            return await self.private_message_service.edit_description(interaction)
        if interaction.data['custom_id'] == 'button_games':
            return await self.private_message_service.edit_games(interaction)
        if interaction.data['custom_id'] == 'button_opposite_gender':
            return await self.private_message_service.edit_opposite_gender(interaction)
        if interaction.data['custom_id'] == 'button_gender':
            return await self.private_message_service.edit_gender(interaction)
        if interaction.data['custom_id'] == 'button_age':
            return await self.private_message_service.edit_age(interaction)
        if interaction.data['custom_id'] == 'button_name':
            return await self.private_message_service.edit_name(interaction)
        if interaction.data['custom_id'] == 'find_form':
            # todo - поки що працює
            fetch_user = user_system.fetch_variables_by_user(user=interaction.user)
            return await self.matchmaking_service.find_user_profile(interaction, fetch_user)

        if interaction.data['custom_id'] == 'button_name':
            return await self.private_message_service.edit_name(interaction)
        if interaction.data['custom_id'] == 'button_age':
            return await self.private_message_service.edit_age(interaction)
        if interaction.data['custom_id'] == 'button_gender':
            return await self.private_message_service.edit_gender(interaction)
        if interaction.data['custom_id'] == 'button_opposite_gender':
            return await self.private_message_service.edit_opposite_gender(interaction)
        if interaction.data['custom_id'] == 'button_location':
            return await self.private_message_service.edit_location(interaction)
        if interaction.data['custom_id'] == 'button_games':
            return await self.private_message_service.edit_games(interaction)
        if interaction.data['custom_id'] == 'button_description':
            return await self.private_message_service.edit_description(interaction)
        if interaction.data['custom_id'] == 'button_photo':
            return await self.private_message_service.edit_photo(interaction)
        if interaction.data['custom_id'] == 'button_back':
            return await self.private_message_service.back_to_menu(interaction)


def setup(bot):
    bot.add_cog(DefaultUser(bot))
