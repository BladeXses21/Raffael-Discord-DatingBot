import discord
from discord.ext import commands
from discord import Bot, Interaction

from cog.base import BaseCog
from database.system.user_form import user_system
from extension.logger import logger

from config import GUILD_IDS
from service.private_message_service import PrivateMessageService
from templates.localization.translations import translate_text


class DefaultUser(BaseCog):
    def __init__(self, client: Bot):
        super().__init__(client)
        self.private_message_service = PrivateMessageService(client)
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
        if interaction.data['custom_id'] == 'find_form':
            user_data = user_system.fetch_variables_by_user(interaction.user)
            return await self.matchmaking_service.find_user_profile(interaction, user_data)
        pass


def setup(bot):
    bot.add_cog(DefaultUser(bot))
