import discord
from discord.ext import commands
from discord import Interaction, Option, Bot

from cog.base import BaseCog
from extension.logger import logger

from config import GUILD_IDS, PERMISSIONS_ROLE_FOR_USER, MAIN_CHANNEL_ID
from main import client
from service.privete_message_service import PrivateMessageService


class DefaultUser(BaseCog):
    def __init__(self, client: Bot):
        super().__init__(client)
        self.private_message_service = PrivateMessageService(client)
        logger.info("Cog DefaultUser connected")

    user = discord.SlashCommandGroup('user', 'default command for user', guild_ids=[*GUILD_IDS])

    @commands.command(aliases=['старт'])
    async def start(self, interaction):
        if isinstance(interaction.channel, discord.DMChannel):
            await self.private_message_service.mainMenu(interaction)
        return

    @user.command(name='starting', description='Start')
    @commands.has_any_role(*PERMISSIONS_ROLE_FOR_USER)
    async def starting(self, interaction: Interaction):
        await interaction.response.send_message('success', ephemeral=True)
        return await interaction.user.send('start')


def setup(bot):
    bot.add_cog(DefaultUser(bot))
