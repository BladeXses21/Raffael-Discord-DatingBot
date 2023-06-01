from discord.ui import View
from embed.button.buttons import buttons
from message_template.translations import translate_text


class LetsGoView(View):
    def __init__(self, presentation_two, user_language):
        super().__init__(timeout=None)
        buttons.lets_go_button.label = translate_text("👌 давай почнемо", user_language)
        buttons.lets_go_button.callback = presentation_two
        self.add_item(buttons.lets_go_button)
