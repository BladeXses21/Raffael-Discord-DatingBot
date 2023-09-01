import discord
import os
from discord.ext import commands

from config import PREFIX, TOKEN
from extension.logger import logger

# initialize the bot
client = commands.Bot(command_prefix=PREFIX,
                      help_command=None,
                      intents=discord.Intents.all())


@client.event
async def on_ready():
    logger.info('READY')


@client.event
async def on_command_error(ctx, error):
    if type(error) == commands.CommandNotFound:
        return
    if type(error) == TimeoutError:
        return
    if isinstance(error, commands.CommandOnCooldown):
        return
    logger.error(f'{str(ctx.author)} | {ctx.message.content}')
    logger.error(error)


for filename in os.listdir("cog"):
    if filename.endswith(".py"):
        client.load_extension(f"cog.{filename[:-3]}")


# launch the bot
def start_bot():
    client.run(TOKEN)


if __name__ == "__main__":
    # launch the function start_bot()
    start_bot()
