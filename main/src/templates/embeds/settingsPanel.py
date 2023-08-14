from discord import Embed

from config import emoji_font, emoji_age, emoji_back, emoji_description, emoji_games, emoji_gender, emoji_opposite_gender, \
    emoji_name, emoji_photo, emoji_location
from templates.localization.translations import translate_text


# todo - прикрасити панель керування емодзі які були добавлені, опис вже добавлений у локалізацію uk
class SettingsEmbed(object):
    def __init__(self, user_language):
        self._embed = Embed(
            title=f"**{translate_text('settings', user_language)}**",
            color=3092790,
            description=f"\n{emoji_font}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ{emoji_font}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ{emoji_font}\n"
        )
        self._embed.add_field(value=f"{emoji_name}{emoji_font}—{emoji_font}{translate_text('edit_name', user_language)}", name="", inline=True)
        self._embed.add_field(value=f"{emoji_age}{emoji_font}—{emoji_font}{translate_text('edit_age', user_language)}", name="", inline=True)
        self._embed.add_field(name="", value="ㅤ", inline=True)
        self._embed.add_field(value=f"{emoji_gender}{emoji_font}—{emoji_font}{translate_text('edit_gender', user_language)}", name="", inline=True)
        self._embed.add_field(value=f"{emoji_opposite_gender}{emoji_font}—{emoji_font}{translate_text('edit_opposite_gender', user_language)}",
                              name="", inline=True)
        self._embed.add_field(name="", value="ㅤ", inline=True)
        self._embed.add_field(value=f"{emoji_location}{emoji_font}—{emoji_font}{translate_text('edit_location', user_language)}", name="",
                              inline=True)
        self._embed.add_field(value=f"{emoji_games}{emoji_font}—{emoji_font}{translate_text('edit_game', user_language)}", name="", inline=True)
        self._embed.add_field(name="", value="ㅤ", inline=True)
        self._embed.add_field(value=f"{emoji_description}{emoji_font}—{emoji_font}{translate_text('edit_description', user_language)}", name="",
                              inline=True)
        self._embed.add_field(value=f"{emoji_photo}{emoji_font}—{emoji_font}{translate_text('edit_photo', user_language)}", name="", inline=True)
        self._embed.add_field(name="", value="ㅤ", inline=True)
        self._embed.add_field(value=f"{emoji_back}{emoji_font}—{emoji_font}{translate_text('back', user_language)}", name="", inline=True)

    @property
    def embed(self):
        return self._embed
