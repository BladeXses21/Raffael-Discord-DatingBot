from discord.ui import Button
from discord import ButtonStyle


class Buttons:
    def __init__(self):
        self.create_form = Button(style=ButtonStyle.secondary, label="Create", custom_id='create_form')
        self.look_form = Button(style=ButtonStyle.secondary, label="Look", custom_id='look_form')
        self.delete_form = Button(style=ButtonStyle.secondary, label="Delete", custom_id='delete_form')
        self.share_form = Button(style=ButtonStyle.secondary, label="Share", custom_id='share_form')

        self.woman = Button(style=ButtonStyle.secondary, label="woman")
        self.man = Button(style=ButtonStyle.secondary, label="man")

        self.accept_button = Button(style=ButtonStyle.blurple, label="Click")

        self.lets_go_button = Button(style=ButtonStyle.secondary, label='👌 давай почнемо')

        self.start_dating = Button(style=ButtonStyle.secondary, label='👌 почнімо знайомство', custom_id='start_dating')

        self.ok_button = Button(style=ButtonStyle.secondary, label='👌 Ok')

        self.no_stop = Button(style=ButtonStyle.secondary, label='No stop')


buttons = Buttons()
