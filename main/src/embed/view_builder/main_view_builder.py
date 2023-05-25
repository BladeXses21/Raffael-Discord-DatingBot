from discord.ui import View
from embed.button.buttons import buttons


class MainMenuView(View):
    def __init__(self, create_form, look_form, delete_form, share_form):
        super().__init__(timeout=None)
        buttons.create_form.callback = create_form
        buttons.look_form.callback = look_form
        buttons.delete_form.callback = delete_form
        buttons.share_form.callback = share_form
        self.add_item(buttons.create_form)
        self.add_item(buttons.look_form)
        self.add_item(buttons.delete_form)
        self.add_item(buttons.share_form)
