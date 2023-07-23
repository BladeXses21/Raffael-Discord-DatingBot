from discord.ui import Button
from discord import ButtonStyle


class Buttons:
    def __init__(self):
        self.create_form = Button(style=ButtonStyle.secondary, label="Create")
        self.look_form = Button(style=ButtonStyle.secondary, label="Look")
        self.delete_form = Button(style=ButtonStyle.secondary, label="Delete")
        self.share_form = Button(style=ButtonStyle.secondary, label="Share")

        self.woman = Button(style=ButtonStyle.secondary, label="woman")
        self.man = Button(style=ButtonStyle.secondary, label="man")

        self.accept_button = Button(style=ButtonStyle.blurple, label="Click")

        self.lets_go_button = Button(style=ButtonStyle.secondary, label='👌 давай почнемо')

        self.ok_button = Button(style=ButtonStyle.secondary, label='👌 Ok')

        self.no_stop = Button(style=ButtonStyle.secondary, label='No stop')


buttons = Buttons()
