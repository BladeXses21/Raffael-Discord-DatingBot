from discord.ui import View

from templates.button.buttons import buttons
from templates.translation_msg.translations import translate_text


class TryAgainView(View):
    def __init__(self, create_form, cancel_create_form, user_language):
        super().__init__(timeout=None)
        buttons.lets_go_button.label = translate_text("👌 давай почнемо", user_language)
        buttons.no_stop.label = translate_text("ні, зупинитись", user_language)
        buttons.lets_go_button.callback = create_form
        buttons.no_stop.callback = cancel_create_form
        self.add_item(buttons.lets_go_button)
        self.add_item(buttons.no_stop)
