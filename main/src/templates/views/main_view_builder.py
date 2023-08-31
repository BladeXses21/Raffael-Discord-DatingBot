from discord.ui import View

from templates.button.buttons import buttons


class MainMenuView(View):
    def __init__(self, share_form):
        super().__init__(timeout=None)
        buttons.button_share.callback = share_form
        self.add_item(buttons.button_fill_form)
        self.add_item(buttons.button_search_profiles)
        self.add_item(buttons.button_view_profile)
        self.add_item(buttons.button_settings)
        self.add_item(buttons.button_share)
