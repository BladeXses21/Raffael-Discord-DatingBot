from discord.ui import Button
from discord import ButtonStyle

from config import emoji_fill_form, emoji_search_profiles, emoji_view_profile, emoji_settings, emoji_share, emoji_next_profile, emoji_stop_search, \
    emoji_like, emoji_talk_together, emoji_report_profile, emoji_block_profile, emoji_thumbs_up


# todo - add all emoji

class Buttons:
    def __init__(self):
        self.button_fill_form = Button(style=ButtonStyle.secondary, custom_id='create_form', emoji=emoji_fill_form)
        self.button_search_profiles = Button(style=ButtonStyle.secondary, custom_id='find_form', emoji=emoji_search_profiles)
        self.button_view_profile = Button(style=ButtonStyle.secondary, custom_id='look_form', emoji=emoji_view_profile)
        self.button_settings = Button(style=ButtonStyle.secondary, custom_id='settings_form', emoji=emoji_settings)
        self.button_share = Button(style=ButtonStyle.secondary, custom_id='share_form', emoji=emoji_share)
        self.button_talk_together = Button(style=ButtonStyle.secondary, custom_id='talk_together', emoji=emoji_talk_together)

        self.button_next_profile = Button(style=ButtonStyle.secondary, custom_id='next_form', emoji=emoji_next_profile)
        self.button_stop_search = Button(style=ButtonStyle.secondary, custom_id='stop_search', emoji=emoji_stop_search)
        self.button_like = Button(style=ButtonStyle.secondary, custom_id='like', emoji=emoji_like)
        self.button_report_profile = Button(style=ButtonStyle.secondary, custom_id='report_profile', emoji=emoji_report_profile)
        self.button_block_profile = Button(style=ButtonStyle.secondary, custom_id='block_profile', emoji=emoji_block_profile)
        self.button_thumbs_up = Button(style=ButtonStyle.secondary, custom_id='thumbs_up', emoji=emoji_thumbs_up)
        self.woman = Button(style=ButtonStyle.secondary, label="woman")
        self.man = Button(style=ButtonStyle.secondary, label="man")
        self.accept_button = Button(style=ButtonStyle.blurple, label="click")
        self.lets_go_button = Button(style=ButtonStyle.secondary, label='click_start')

        self.start_dating = Button(style=ButtonStyle.secondary, label='start_dating', custom_id='start_dating')
        self.ok_button = Button(style=ButtonStyle.secondary, label='👌 Ok')
        self.no_stop = Button(style=ButtonStyle.secondary, label='stop')


buttons = Buttons()
