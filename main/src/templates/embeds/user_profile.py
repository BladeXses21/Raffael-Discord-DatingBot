from discord import Embed

from model.user_model.user import UserModel
from templates.message_template.translations import translate_text, get_translated_gender


class UserProfileEmbed(object):
    def __init__(self, user: UserModel):
        gender_emote = get_translated_gender(user.user_gender, user.user_language)
        self._embed = Embed(
            color=3092790
        )
        self._embed.add_field(name=f"{translate_text('Уподобайки:', user.user_likes)}", value=f"{user.user_likes}❤", inline=False)
        self._embed.add_field(name=translate_text("Ім'я:", user.user_language), value=f"{user.user_name}, {gender_emote}", inline=False)
        self._embed.add_field(name=translate_text('Вік:', user.user_language), value=str(user.user_age), inline=False)
        self._embed.add_field(name=translate_text('Місто:', user.user_language), value=str(user.user_location), inline=False)
        self._embed.add_field(name=translate_text('Ігри:', user.user_language), value=str(user.user_games), inline=False)
        self._embed.set_image(url=str(user.user_photo))
        self._embed.description = str(user.user_description)

    @property
    def embed(self):
        return self._embed

    # todo - забрати усі філди і запихнути все в дескріпшин виставляючи все по порядку
