from discord import Embed

from model.user_model.user import UserForm
from templates.localization.translations import translate_text, get_gender_emoji
from utils.funcs import get_city_from_coordinates


class UserProfileEmbed(object):
    def __init__(self, user):
        user_dict = UserForm.parse_obj(user)
        self._embed = Embed(
            color=3092790,
            description=f"**{translate_text('likes', user_dict.language)}: {user_dict.likes}❤**\n\n"
                        f"**{translate_text('name', user_dict.language)}:** {user_dict.name}, {get_gender_emoji(user_dict.gender)}\n"
                        f"**{translate_text('age', user_dict.language)}:** {user_dict.age}\n\n"
                        f"**{translate_text('city', user_dict.language)}:** {str(get_city_from_coordinates(user_dict.location[0], user_dict.location[1]))}\n\n"
                        f"**{translate_text('games', user_dict.language)}:** {user_dict.games}\n\n"
                        f"{user_dict.description}\n"
        )
        self._embed.set_image(url=str(user_dict.photo))

    @property
    def embed(self):
        return self._embed