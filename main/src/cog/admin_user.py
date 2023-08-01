import discord
from discord.ext import commands
from discord import Bot, Interaction

from cog.base import BaseCog
from config import GUILD_IDS
from extension.logger import logger
from service.private_message_service import PrivateMessageService
from templates.localization.translations import translate_text
from templates.view_builder.start_dating import StartDating


class AdminUser(BaseCog):
    def __init__(self, client: Bot):
        super().__init__(client)
        logger.info("Cog AdminUser connected")
        self.private_message_service = PrivateMessageService(client)

    admin = discord.SlashCommandGroup('admin', 'default command for admin', guild_ids=[*GUILD_IDS])

    @admin.command()
    async def meet(self, interaction: Interaction):
        user_language = interaction.locale
        start_dating_view = StartDating(language=user_language)
        embed = discord.Embed(title="Meet the Admin", description="Hello! I'm the admin of this server. How can I help you today?")
        await interaction.response.send_message(embed=embed, view=start_dating_view)

    @commands.Cog.listener()
    async def on_interaction(self, interaction: Interaction):
        user_language = interaction.locale
        if interaction.data['custom_id'] == 'start_dating':
            await self.private_message_service.user_name(interaction)
            return await interaction.response.send_message(content=translate_text('check_private_messages', user_language), ephemeral=True)
        if interaction.data['custom_id'] == 'create_form':
            return await self.private_message_service.user_name(interaction)
        if interaction.data['custom_id'] == 'look_form':
            return await self.private_message_service.user_profile(interaction)
        pass


def setup(bot):
    bot.add_cog(AdminUser(bot))
