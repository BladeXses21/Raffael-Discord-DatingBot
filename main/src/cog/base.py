from discord import Cog, Bot


class BaseCog(Cog):
    def __init__(self, client: Bot):
        self.client = client
        self.guild = None


def setup(bot):
    bot.add_cog(BaseCog(bot))
