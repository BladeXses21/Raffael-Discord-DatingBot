from discord.ui import View

from templates.button.buttons import buttons


class DatingMenuView(View):
    def __init__(self, like_user, block_user, next_user, report_user, stop_search, thumbs_up_user):
        super().__init__(timeout=None)
        buttons.button_like.callback = like_user
        buttons.button_block_profile.callback = block_user
        buttons.button_next_profile.callback = next_user
        buttons.button_report_profile.callback = report_user
        buttons.button_stop_search.callback = stop_search
        buttons.button_thumbs_up.callback = thumbs_up_user
        self.add_item(buttons.button_like)
        self.add_item(buttons.button_block_profile)
        self.add_item(buttons.button_next_profile)
        self.add_item(buttons.button_report_profile)
        self.add_item(buttons.button_stop_search)
        self.add_item(buttons.button_thumbs_up)
