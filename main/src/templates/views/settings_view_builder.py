from discord.ui import View

from templates.button.buttons import buttons


class SettingsMenuView(View):
    def __init__(self, name, age, gender, opposite_gender, location, games, description, photo, back):
        super().__init__(timeout=None)
        buttons.name_button.callback = name
        buttons.age_button.callback = age
        buttons.gender_button.callback = gender
        buttons.opposite_gender_button.callback = opposite_gender
        buttons.location_button.callback = location
        buttons.games_button.callback = games
        buttons.description_button.callback = description
        buttons.photo_button.callback = photo
        buttons.back_button.callback = back
        self.add_item(buttons.name_button)
        self.add_item(buttons.age_button)
        self.add_item(buttons.gender_button)
        self.add_item(buttons.opposite_gender_button)
        self.add_item(buttons.location_button)
        self.add_item(buttons.games_button)
        self.add_item(buttons.description_button)
        self.add_item(buttons.photo_button)
        self.add_item(buttons.back_button)
