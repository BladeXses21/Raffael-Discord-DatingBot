from discord.ui import View

from templates.button.buttons import buttons


class MainMenuView(View):
    def __init__(self, create_form, find_form, look_form, settings_form, share_form):
        super().__init__(timeout=None)
        buttons.create_form.callback = create_form
        buttons.find_form.callback = find_form
        buttons.look_form.callback = look_form
        buttons.settings_form.callback = settings_form
        buttons.share_form.callback = share_form
        self.add_item(buttons.create_form)
        self.add_item(buttons.find_form)
        self.add_item(buttons.look_form)
        self.add_item(buttons.settings_form)
        self.add_item(buttons.share_form)
