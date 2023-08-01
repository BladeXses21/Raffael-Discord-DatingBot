from discord import Embed


class Profile(object):
    def __init__(self, rating: int, description: str):
        self._embed = Embed(
            title=f'Рейтинг: {str(rating)}',
            description=str(description),
        )
        self._embed.add_field(name="name", value='', inline=False)
        self._embed.add_field(name='age', value='', inline=False)
        self._embed.add_field(name='city', value='', inline=False)
        self._embed.add_field(name='games', value='', inline=False)

    @property
    def embed(self):
        return self._embed
