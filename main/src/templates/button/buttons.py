from discord.ui import Button
from discord import ButtonStyle


# todo - add all emoji

class Buttons:
    def __init__(self):
        self.create_form = Button(style=ButtonStyle.secondary, custom_id='create_form', emoji="<:start_raffael:1135940939995697212>")
        self.find_form = Button(style=ButtonStyle.secondary, custom_id='find_form', emoji="<:find_raffael:1135940929463799920>")
        self.look_form = Button(style=ButtonStyle.secondary, label="Look", custom_id='look_form', emoji="<:profile_raffael:1135940938414432337>")
        self.settings_form = Button(style=ButtonStyle.secondary, label="Delete", custom_id='delete_form', emoji="<:settings_raffael:1135940931120529438>")
        self.share_form = Button(style=ButtonStyle.secondary, label="Share", custom_id='share_form', emoji="<:twoheart_raffael:1135940944668131449>")

        self.woman = Button(style=ButtonStyle.secondary, label="woman")
        self.man = Button(style=ButtonStyle.secondary, label="man")
        self.accept_button = Button(style=ButtonStyle.blurple, label="click")
        self.lets_go_button = Button(style=ButtonStyle.secondary, label='click_start')

        self.start_dating = Button(style=ButtonStyle.secondary, label='start_dating', custom_id='start_dating')
        self.ok_button = Button(style=ButtonStyle.secondary, label='👌 Ok')
        self.no_stop = Button(style=ButtonStyle.secondary, label='stop')


buttons = Buttons()
