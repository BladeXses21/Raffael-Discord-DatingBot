from discord import Embed

from config import emoji_talk_together_url, emoji_fill_form, emoji_block_profile, emoji_report_profile, emoji_search_profiles, emoji_settings, \
    emoji_like, emoji_view_profile, emoji_share, emoji_next_profile, emoji_stop_search, emoji_font
from templates.localization.translations import translate_text


# todo - прикрасити панель керування смайлами
class MainPanelEmbed(object):
    def __init__(self, user_language):
        self._embed = Embed(
            title=f"**{translate_text('control_panel', user_language)}**",
            color=3092790,
            description=f"\n{emoji_font}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ{emoji_font}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ{emoji_font}\n"
        ).set_footer(text=translate_text("together", user_language), icon_url=emoji_talk_together_url)
        self._embed.add_field(value=f"{emoji_fill_form}{emoji_font}—{emoji_font}{translate_text('fill_form', user_language)}", name='', inline=True)
        self._embed.add_field(value=f"{emoji_block_profile}{emoji_font}—{emoji_font}{translate_text('block', user_language)}", name='', inline=True)
        self._embed.add_field(name="", value="ㅤ", inline=True)
        self._embed.add_field(value=f"{emoji_search_profiles}{emoji_font}—{emoji_font}{translate_text('find_partner', user_language)}", name='',
                              inline=True)
        self._embed.add_field(value=f"{emoji_report_profile}{emoji_font}—{emoji_font}{translate_text('complain', user_language)}", name='',
                              inline=True)
        self._embed.add_field(name="", value="ㅤ", inline=True)
        self._embed.add_field(value=f"{emoji_view_profile}{emoji_font}—{emoji_font}{translate_text('view_profile', user_language)}", name='',
                              inline=True)
        self._embed.add_field(value=f"{emoji_like}{emoji_font}—{emoji_font}{translate_text('like', user_language)}", name='', inline=True)
        self._embed.add_field(name="", value="ㅤ", inline=True)
        self._embed.add_field(value=f"{emoji_settings}{emoji_font}—{emoji_font}{translate_text('settings', user_language)}", name='', inline=True)
        self._embed.add_field(value=f"{emoji_next_profile}{emoji_font}—{emoji_font}{translate_text('skip', user_language)}", name='', inline=True)
        self._embed.add_field(name="", value="ㅤ", inline=True)
        self._embed.add_field(value=f"{emoji_share}{emoji_font}—{emoji_font}{translate_text('share', user_language)}", name='', inline=True)
        self._embed.add_field(value=f"{emoji_stop_search}{emoji_font}—{emoji_font}{translate_text('stop_search', user_language)}", name='',
                              inline=True)
        self._embed.add_field(name="", value="ㅤ", inline=True)

    @property
    def embed(self):
        return self._embed
