from discord import Embed

from config import emoji_talk_together_url, emoji_fill_form, emoji_block_profile, emoji_report_profile, emoji_search_profiles, emoji_settings, \
    emoji_like, emoji_view_profile, emoji_share, emoji_next_profile, emoji_stop_search
from templates.localization.translations import translate_text


# todo - прикрасити панель керування смайлами
class MainPanelEmbed(object):
    def __init__(self, user_language):
        self._embed = Embed(
            title=translate_text('control_panel', user_language),
            color=3092790,
        ).set_footer(text=translate_text("together", user_language), icon_url=emoji_talk_together_url)
        self._embed.add_field(name=f"{emoji_fill_form}ㅤ—ㅤ{translate_text('fill_form', user_language)}", value='', inline=True)
        self._embed.add_field(name=f"{emoji_block_profile}ㅤ—ㅤ{translate_text('block', user_language)}", value='', inline=True)
        self._embed.add_field(name="", value="ㅤ", inline=True)
        self._embed.add_field(name=f"{emoji_search_profiles}ㅤ—ㅤ{translate_text('find_partner', user_language)}", value='', inline=True)
        self._embed.add_field(name=f"{emoji_report_profile}ㅤ—ㅤ{translate_text('complain', user_language)}", value='', inline=True)
        self._embed.add_field(name="", value="ㅤ", inline=True)
        self._embed.add_field(name=f"{emoji_view_profile}ㅤ—ㅤ{translate_text('view_profile', user_language)}", value='', inline=True)
        self._embed.add_field(name=f"{emoji_like}ㅤ—ㅤ{translate_text('like', user_language)}", value='', inline=True)
        self._embed.add_field(name="", value="ㅤ", inline=True)
        self._embed.add_field(name=f"{emoji_settings}ㅤ—ㅤ{translate_text('settings', user_language)}", value='', inline=True)
        self._embed.add_field(name=f"{emoji_next_profile}ㅤ—ㅤ{translate_text('skip', user_language)}", value='', inline=True)
        self._embed.add_field(name="", value="ㅤ", inline=True)
        self._embed.add_field(name=f"{emoji_share}ㅤ—ㅤ{translate_text('share', user_language)}", value='', inline=True)
        self._embed.add_field(name=f"{emoji_stop_search}ㅤ—ㅤ{translate_text('stop_search', user_language)}", value='', inline=True)
        self._embed.add_field(name="", value="ㅤ", inline=True)

    @property
    def embed(self):
        return self._embed
