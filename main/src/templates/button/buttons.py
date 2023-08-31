from discord.ui import Button
from discord import ButtonStyle

from config import emoji_fill_form, emoji_search_profiles, emoji_view_profile, emoji_settings, emoji_share, emoji_next_profile, emoji_stop_search, \
    emoji_like, emoji_talk_together, emoji_report_profile, emoji_block_profile, emoji_thumbs_up, emoji_name, emoji_age, emoji_gender, \
    emoji_opposite_gender, emoji_location, emoji_games, emoji_description, emoji_photo, emoji_back


# todo - add all emoji

class Buttons:
    def __init__(self):
        # button_fill_form: This button opens the form for filling out personal information.
        self.button_fill_form = Button(style=ButtonStyle.secondary, custom_id='create_form', emoji=emoji_fill_form)
        # button_search_profiles: This button opens the search for profiles.
        self.button_search_profiles = Button(style=ButtonStyle.secondary, custom_id='find_form', emoji=emoji_search_profiles)
        # button_view_profile: This button opens the profile of the selected user.
        self.button_view_profile = Button(style=ButtonStyle.secondary, custom_id='look_form', emoji=emoji_view_profile)
        # button_settings: This button opens the settings.
        self.button_settings = Button(style=ButtonStyle.secondary, custom_id='settings_form', emoji=emoji_settings)
        # button_share: This button shares the bot with other users.
        self.button_share = Button(style=ButtonStyle.secondary, custom_id='share_form', emoji=emoji_share)
        # button_talk_together: This button starts a chat with the selected user.
        self.button_talk_together = Button(style=ButtonStyle.secondary, custom_id='talk_together', emoji=emoji_talk_together)
        # button_next_profile: This button goes to the next profile in the search results.
        self.button_next_profile = Button(style=ButtonStyle.secondary, custom_id='next_form', emoji=emoji_next_profile)
        # button_stop_search: This button stops the search and closes the search results.
        self.button_stop_search = Button(style=ButtonStyle.secondary, custom_id='stop_search', emoji=emoji_stop_search)
        # button_like: This button likes the selected profile.
        self.button_like = Button(style=ButtonStyle.secondary, custom_id='like', emoji=emoji_like)
        # button_report_profile: This button reports the selected profile.
        self.button_report_profile = Button(style=ButtonStyle.secondary, custom_id='report_profile', emoji=emoji_report_profile)
        # button_block_profile: This button blocks the selected profile.
        self.button_block_profile = Button(style=ButtonStyle.secondary, custom_id='block_profile', emoji=emoji_block_profile)
        # button_thumbs_up: This button gives a thumbs up to the selected profile.
        self.button_thumbs_up = Button(style=ButtonStyle.secondary, custom_id='thumbs_up', emoji=emoji_thumbs_up)
        # woman: This button selects the woman gender.
        self.woman = Button(style=ButtonStyle.secondary, label="woman")
        # man: This button selects the man gender.
        self.man = Button(style=ButtonStyle.secondary, label="man")
        # accept_button: This button accepts the terms and conditions.
        self.accept_button = Button(style=ButtonStyle.blurple, label="click")
        # lets_go_button: This button starts the dating process.
        self.lets_go_button = Button(style=ButtonStyle.secondary, label='click_start')
        # start_dating: This button starts the dating process.
        self.start_dating = Button(style=ButtonStyle.secondary, label='start_dating', custom_id='start_dating')
        # ok_button: This button confirms the action.
        self.ok_button = Button(style=ButtonStyle.secondary, label='👌 Ok', custom_id='button_ok')
        # no_stop: This button cancels the action.
        self.no_stop = Button(style=ButtonStyle.secondary, label='stop', custom_id='button_stop')
        # name_button: This button to change the name
        self.name_button = Button(style=ButtonStyle.secondary, emoji=emoji_name, custom_id='button_name')
        # age_button: This button to change the age
        self.age_button = Button(style=ButtonStyle.secondary, emoji=emoji_age, custom_id='button_age')
        # gender_button: This button to change the gender
        self.gender_button = Button(style=ButtonStyle.secondary, emoji=emoji_gender, custom_id='button_gender')
        # opposite_gender_button: This button to change the opposite gender
        self.opposite_gender_button = Button(style=ButtonStyle.secondary, emoji=emoji_opposite_gender, custom_id='button_opposite_gender')
        # location_button: This button to change the location
        self.location_button = Button(style=ButtonStyle.secondary, emoji=emoji_location, custom_id='button_location')
        # games_button: This button to change the games
        self.games_button = Button(style=ButtonStyle.secondary, emoji=emoji_games, custom_id='button_games')
        # description_button: This button to change the description
        self.description_button = Button(style=ButtonStyle.secondary, emoji=emoji_description, custom_id='button_description')
        # photo_button: This button to change the photo
        self.photo_button = Button(style=ButtonStyle.secondary, emoji=emoji_photo, custom_id='button_photo')
        # back_button: button to return to the previous menu
        self.back_button = Button(style=ButtonStyle.secondary, emoji=emoji_back, custom_id='button_back')


buttons = Buttons()
