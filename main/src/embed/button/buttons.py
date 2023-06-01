from discord.ui import Button
from discord import ButtonStyle

from message_template.translations import translate_text


class Buttons:
    def __init__(self):
        self.create_form = Button(style=ButtonStyle.secondary, label="Create")
        self.look_form = Button(style=ButtonStyle.secondary, label="Look")
        self.delete_form = Button(style=ButtonStyle.secondary, label="Delete")
        self.share_form = Button(style=ButtonStyle.secondary, label="Share")

        self.woman = Button(style=ButtonStyle.secondary, label="woman")
        self.man = Button(style=ButtonStyle.secondary, label="man")

        self.accept_button = Button(style=ButtonStyle.green, label="Click")

        self.lets_go_button = Button(style=ButtonStyle.secondary, label='👌 давай почнемо')


buttons = Buttons()
