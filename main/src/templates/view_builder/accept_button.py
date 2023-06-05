from discord.ui import View

from templates.button.buttons import buttons


class StartConfirmation(View):
    def __init__(self, control_panel):
        super().__init__(timeout=None)
        buttons.accept_button.callback = control_panel
        self.add_item(buttons.accept_button)
