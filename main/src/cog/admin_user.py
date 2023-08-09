import discord
from discord import Bot, Interaction

from cog.base import BaseCog
from config import GUILD_IDS
from extension.logger import logger
from service.matchmaking_service import MatchmakingService
from service.private_message_service import PrivateMessageService
from templates.view_builder.start_dating import StartDating


class AdminUser(BaseCog):
    def __init__(self, client: Bot):
        super().__init__(client)
        logger.info("Cog AdminUser connected")
        self.private_message_service = PrivateMessageService(client)
        self.matchmaking_service = MatchmakingService(client)

    admin = discord.SlashCommandGroup('admin', 'default command for admin', guild_ids=[*GUILD_IDS])

    @admin.command()
    async def meet(self, interaction: Interaction):
        user_language = interaction.locale
        start_dating_view = StartDating(language=user_language)
        embed = discord.Embed(title="Meet the Admin", description="Hello! I'm the admin of this server. How can I help you today?")
        await interaction.response.send_message(embed=embed, view=start_dating_view)


def setup(bot):
    bot.add_cog(AdminUser(bot))
