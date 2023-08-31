from json import JSONDecodeError

import discord
from discord import Bot, Interaction, ApplicationContext
from discord.ext import commands

from cog.base import BaseCog
from config import GUILD_IDS, PERMISSIONS_ROLE_FOR_USER
from extension.logger import logger
from service.matchmaking_service import MatchmakingService
from service.private_message_service import PrivateMessageService
from templates.embeds.base import DefaultEmbed
from templates.views.start_dating_view_builder import StartDating
from utils.funcs import get_embed


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

    @commands.command(description='Відправка ембеда')
    @commands.has_any_role(*PERMISSIONS_ROLE_FOR_USER)
    async def emb(self, ctx: ApplicationContext, *, args):
        try:
            embed = get_embed(args)
            await ctx.send(embed=embed)
            return await ctx.message.delete()

        except JSONDecodeError as e:
            await ctx.send(embed=DefaultEmbed(f'Error: {str(e)}'))
            return await ctx.message.delete()


def setup(bot):
    bot.add_cog(AdminUser(bot))
