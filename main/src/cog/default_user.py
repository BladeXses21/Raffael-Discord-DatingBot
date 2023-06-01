import discord
from discord.ext import commands
from discord import Interaction, Bot, ApplicationContext

from cog.base import BaseCog
from extension.logger import logger

from config import GUILD_IDS, PERMISSIONS_ROLE_FOR_USER
from main import client
from service.privete_message_service import PrivateMessageService


class DefaultUser(BaseCog):
    def __init__(self, client: Bot):
        super().__init__(client)
        self.private_message_service = PrivateMessageService(client)
        logger.info("Cog DefaultUser connected")

    user = discord.SlashCommandGroup('user', 'default command for user', guild_ids=[*GUILD_IDS])

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "старт" or message.content == "start":
            return await self.private_message_service.language_scanning(message.author)
        else:
            pass

    @commands.command(name='start', description='User command')
    async def start(self, interaction: Interaction):
        if isinstance(interaction.channel, discord.DMChannel):
            await self.private_message_service.control_panel(interaction)
        return

    @user.command(name='usercommand', description='User command')
    @commands.has_any_role(*PERMISSIONS_ROLE_FOR_USER)
    async def usercommand(self, interaction: Interaction):
        await interaction.response.send_message('success', ephemeral=True)
        return await interaction.user.send('start')

    @user.command(name='to', description='toto')
    async def to(self, interaction: Interaction):
        return await interaction.response.send_message('toto')


def setup(bot):
    bot.add_cog(DefaultUser(bot))
