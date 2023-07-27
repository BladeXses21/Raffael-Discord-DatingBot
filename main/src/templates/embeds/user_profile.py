from discord import Embed

from model.user_model.user import UserForm
from templates.translation_msg.translations import translate_text


class UserProfileEmbed(object):
    def __init__(self, user):
        name_word = "Ім'я"
        user_dict = UserForm.parse_obj(user)
        # gender_emote = get_translated_gender(user.gender, user.language)
        self._embed = Embed(
            color=3092790,
            description=f"**{translate_text('Уподобайки', user_dict.language)}: {user_dict.likes}❤**\n\n"
                        f"**{translate_text(name_word, user_dict.language)}:** {user_dict.name}\n"
                        f"**{translate_text('Вік', user_dict.language)}:** {user_dict.age}\n\n"
                        f"**{translate_text('Місто', user_dict.language)}:** {user_dict.location}\n\n"
                        f"**{translate_text('Ігри', user_dict.language)}:** {user_dict.games}\n\n"
                        f"{user_dict.description}\n"
        )
        self._embed.set_image(url=str(user_dict.photo))

    @property
    def embed(self):
        return self._embed

    # todo - забрати усі філди і запихнути все в дескріпшин виставляючи все по порядку
