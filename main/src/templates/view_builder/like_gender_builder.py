from discord.ui import View
from template.button.buttons import buttons


class ChoseLikeGender(View):
    def __init__(self, user_like_woman, user_like_man):
        super().__init__(timeout=None)
        buttons.woman.callback = user_like_woman
        buttons.man.callback = user_like_man
        self.add_item(buttons.woman)
        self.add_item(buttons.man)
