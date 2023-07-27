from discord.ui import View

from templates.button.buttons import buttons


class StartDating(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(buttons.start_dating)
