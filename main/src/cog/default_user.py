import discord
from discord.ext import commands
from discord import Bot

from cog.base import BaseCog
from extension.logger import logger

from config import GUILD_IDS
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
        pass


def setup(bot):
    bot.add_cog(DefaultUser(bot))
