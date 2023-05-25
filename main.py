import discord
import os
from discord.ext import commands

from config import PREFIX, TOKEN, MAIN_CHANNEL_ID
from embed.embeds.welcome import WelcomePrivateMessage
from extension.logger import logger
from service.privete_message_service import PrivateMessageService

client = commands.Bot(command_prefix=PREFIX,
                      help_command=None,
                      intents=discord.Intents.all())


@client.event
async def on_ready():
    logger.info('READY')


# @client.event
# async def on_message(message):
#     if message.channel.id == MAIN_CHANNEL_ID:
#         print(message)
#         if message.content == "старт" or message.content == "start":
#             print("Message")
#             await private_message_service.mainMenu(user=message.author)
#     else:
#         pass


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

private_message_service = PrivateMessageService(client)
client.run(TOKEN)
