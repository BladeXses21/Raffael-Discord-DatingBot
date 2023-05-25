from discord.ui import View
from embed.button.buttons import buttons


class ChoseGenderView(View):
    def __init__(self, user_woman, user_man):
        super().__init__(timeout=None)
        buttons.woman.callback = user_woman
        buttons.man.callback = user_man
        self.add_item(buttons.woman)
        self.add_item(buttons.man)
