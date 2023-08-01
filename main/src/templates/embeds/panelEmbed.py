from discord import Embed

from templates.localization.translations import translate_text


# todo - прикрасити панель керування смайлами
class MainPanelEmbed(object):
    def __init__(self, user_language):
        self._embed = Embed(
            title=translate_text('control_panel', user_language),
            color=3092790
        )
        self._embed.add_field(name=translate_text('fill_form', user_language), value='')
        self._embed.add_field(name=translate_text('find_partner', user_language), value='')
        self._embed.add_field(name=translate_text('view_profile', user_language), value='')
        self._embed.add_field(name=translate_text('sleep_mode', user_language), value='')
        self._embed.add_field(name=translate_text('share', user_language), value='')

        self._embed.add_field(name=translate_text('like', user_language), value='')
        self._embed.add_field(name=translate_text('block', user_language), value='')
        self._embed.add_field(name=translate_text('skip', user_language), value='')
        self._embed.add_field(name=translate_text('complain', user_language), value='')
        self._embed.add_field(name=translate_text('stop_search', user_language), value='')

    @property
    def embed(self):
        return self._embed
