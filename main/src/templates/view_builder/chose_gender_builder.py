from discord.ui import View
from template.button.buttons import buttons
from template.message_template.translations import translate_text


class ChoseGenderView(View):
    def __init__(self, user_woman, user_man, user_language=None):
        super().__init__(timeout=None)
        buttons.woman.label = translate_text("Дівчина", user_language)
        buttons.man.label = translate_text("Хлопець", user_language)
        buttons.woman.callback = user_woman
        buttons.man.callback = user_man
        self.add_item(buttons.woman)
        self.add_item(buttons.man)
