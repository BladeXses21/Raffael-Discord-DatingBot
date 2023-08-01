from discord.ui import View

from templates.button.buttons import buttons
from templates.localization.translations import translate_text


class StartDating(View):
    def __init__(self, language):
        super().__init__(timeout=None)
        buttons.start_dating.label = translate_text('start_dating', language)
        self.add_item(buttons.start_dating)
