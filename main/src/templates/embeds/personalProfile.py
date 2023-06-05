from discord import Embed


class Profile(object):
    def __init__(self, rating: int, description: str):
        self._embed = Embed(
            title=f'Рейтинг: {str(rating)}',
            description=str(description),
        )
        self._embed.add_field(name="Ім'я", value='', inline=False)
        self._embed.add_field(name='Вік:', value='', inline=False)
        self._embed.add_field(name='Місто:', value='', inline=False)
        self._embed.add_field(name='Ігри', value='', inline=False)

    @property
    def embed(self):
        return self._embed
