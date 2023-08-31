import discord
from discord.ui import Select

from templates.localization.translations import translate_text


class GenderSelectView(Select):
    def __init__(self, user_language, callback, placeholder):
        gender_options = [
            discord.SelectOption(label=translate_text('Хлопець', user_language), value='boy'),
            discord.SelectOption(label=translate_text('Дівчина', user_language), value='girl'),
            discord.SelectOption(label=translate_text('LGBT', user_language), value='lgbt')
        ]
        super().__init__(custom_id='gender_selection', options=gender_options, placeholder=placeholder, min_values=1, max_values=1)
        self.callback = callback
