from discord import Embed

from model.user_model.user import UserForm
from templates.translation_msg.translations import translate_text, get_translated_gender


class UserProfileEmbed(object):
    def __init__(self, user: UserForm):
        gender_emote = get_translated_gender(user.user_gender, user.language)
        self._embed = Embed(
            color=3092790,
            description=str(user.description),
        )
        self._embed.add_field(name=f"{translate_text('Уподобайки:', user.likes)}", value=f"{user.likes}❤", inline=False)
        self._embed.add_field(name=translate_text("Ім'я:", user.language), value=f"{user.user_name}, {gender_emote}", inline=False)
        self._embed.add_field(name=translate_text('Вік:', user.language), value=str(user.age), inline=False)
        self._embed.add_field(name=translate_text('Місто:', user.language), value=str(user.location), inline=False)
        self._embed.add_field(name=translate_text('Ігри:', user.language), value=str(user.games), inline=False)
        self._embed.set_image(url=str(user.photo))

    @property
    def embed(self):
        return self._embed

    # todo - забрати усі філди і запихнути все в дескріпшин виставляючи все по порядку
