from discord.ui import View

from templates.button.buttons import buttons


class SettingsMenuView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(buttons.name_button)
        self.add_item(buttons.age_button)
        self.add_item(buttons.gender_button)
        self.add_item(buttons.opposite_gender_button)
        self.add_item(buttons.location_button)
        self.add_item(buttons.games_button)
        self.add_item(buttons.description_button)
        self.add_item(buttons.photo_button)
        self.add_item(buttons.back_button)
