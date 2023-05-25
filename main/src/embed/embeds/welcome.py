from discord import Embed


class WelcomePrivateMessage(object):
    def __init__(self):
        self._embed = Embed(
            title='Привіт',
            description='**Це головне меню**',
            color=3092790
        )
        self._embed.add_field(name='Створити/змінити анкету', value='Натисніть 1', inline=False)
        self._embed.add_field(name='Дивитись анкети', value='Натисніть 2', inline=False)
        self._embed.add_field(name='Прибрати мою анкету', value='Натисніть 3', inline=False)
        self._embed.add_field(name='Поділитись із друзями', value='Натисніть 4', inline=False)

    @property
    def embed(self):
        return self._embed
