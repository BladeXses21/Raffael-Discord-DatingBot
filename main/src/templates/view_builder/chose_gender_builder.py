from discord.ui import View

from templates.button.buttons import buttons
from templates.localization.translations import translate_text


class ChoseGenderView(View):
    def __init__(self, user_woman, user_man, user_language=None):
        super().__init__(timeout=None)
        buttons.woman.label = translate_text("gender_boy", user_language)
        buttons.man.label = translate_text("gender_girl", user_language)
        buttons.woman.callback = user_woman
        buttons.man.callback = user_man
        self.add_item(buttons.woman)
        self.add_item(buttons.man)
