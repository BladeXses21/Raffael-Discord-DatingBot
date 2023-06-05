from discord import Embed

from templates.message_template.translations import translate_text


# todo - прикрасити панель керування смайлами
class MainPanelEmbed(object):
    def __init__(self, user_language):
        self._embed = Embed(
            title=translate_text('Панель керування', user_language),
            color=3092790
        )
        self._embed.add_field(name=translate_text('Заповнити анкету.', user_language), value='')
        self._embed.add_field(name=translate_text('Шукати співрозмовника.', user_language), value='')
        self._embed.add_field(name=translate_text('Подивитись профіль.', user_language), value='')
        self._embed.add_field(name=translate_text('Сплячий режим.', user_language), value='')
        self._embed.add_field(name=translate_text('Поділитись.', user_language), value='')

        self._embed.add_field(name=translate_text('Поставити уподобайку.', user_language), value='')
        self._embed.add_field(name=translate_text('Заблокувати.', user_language), value='')
        self._embed.add_field(name=translate_text('Пропустити.', user_language), value='')
        self._embed.add_field(name=translate_text('Поскаржитись.', user_language), value='')
        self._embed.add_field(name=translate_text('Зупинити пошук.', user_language), value='')

    @property
    def embed(self):
        return self._embed
