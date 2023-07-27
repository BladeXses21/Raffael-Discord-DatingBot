import discord
from discord.ext import commands
from discord import Bot, Interaction

from cog.base import BaseCog
from config import GUILD_IDS
from extension.logger import logger
from service.private_message_service import PrivateMessageService
from templates.view_builder.start_dating import StartDating


class AdminUser(BaseCog):
    def __init__(self, client: Bot):
        super().__init__(client)
        logger.info("Cog AdminUser connected")
        self.private_message_service = PrivateMessageService(client)

    admin = discord.SlashCommandGroup('admin', 'default command for admin', guild_ids=[*GUILD_IDS])

    @admin.command()
    async def meet(self, interaction: Interaction):
        start_dating_view = StartDating()
        embed = discord.Embed(title="Meet the Admin", description="Hello! I'm the admin of this server. How can I help you today?")
        await interaction.response.send_message(embed=embed, view=start_dating_view)

    @commands.Cog.listener()
    async def on_interaction(self, interaction: Interaction):
        if interaction.data['custom_id'] == 'start_dating':
            await self.private_message_service.language_scanning(interaction.user)
            return await interaction.response.send_message(content='***`Перевірте особисті повідомлення.`***', ephemeral=True)
        if interaction.data['custom_id'] == 'create_form':
            return await self.private_message_service.user_name(interaction)
        pass


def setup(bot):
    bot.add_cog(AdminUser(bot))
