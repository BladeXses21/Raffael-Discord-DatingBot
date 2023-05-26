import discord.errors
from discord import Interaction
from discord.ui import Select
from config import MIN_AGE, MAX_AGE
from embed.embeds.base import DefaultEmbed
from embed.embeds.welcome import WelcomePrivateMessage
from embed.view_builder.chose_gender_builder import ChoseGenderView
from embed.view_builder.like_gender_builder import ChoseLikeGender
from embed.view_builder.main_view_builder import MainMenuView
from extension.logger import logger
from utils.funcs import check_location

gender_options = [
    discord.SelectOption(label='Хлопець', value='man'),
    discord.SelectOption(label='Дівчина', value='woman'),
    discord.SelectOption(label='ЛГБТ-клуб', value='lgbt')
]


class PrivateMessageService:
    def __init__(self, client):
        self.client = client
        self.USER_AGE = int()
        self.USER_GENDER = str()
        self.USER_LIKE_GENDER = str()
        self.USER_LOCATION = str()
        self.USER_GAMES = str()
        self.USER_DESCRIPTION = str()
        self.USER_PHOTO = str()

        self.function_map = {
            'user_age': self.user_age,
            'user_gender': self.user_gender,
            'like_gender': self.like_gender,
            'user_location': self.user_location,
            'user_games': self.user_games,
            'user_description': self.user_description,
            'user_photo': self.user_photo,
            'form_successfully_created': self.form_successfully_created
        }

        self.function_called = {}

    async def call_function(self, interaction: Interaction, function_name: str):
        print(self.function_called)
        if function_name in self.function_map:
            if function_name in self.function_called and self.function_called[function_name]:
                return False

            self.function_called[function_name] = True
            return await self.function_map[function_name](interaction)

    async def mainMenu(self, interaction):
        logger.info(f'{interaction.author.id} | {interaction.author} викликав mainMenu')

        async def create_form(interact: Interaction):
            self.function_called = {}
            return await self.call_function(interaction=interact, function_name='user_age')

        async def look_form(interact: Interaction):
            return await interact.response.send_message(
                embed=DefaultEmbed(description='**Це повідомлення буде відправлене після натискання кнопки**'))

        async def delete_form(interact: Interaction):
            return await interact.response.send_message(
                embed=DefaultEmbed(description='**Це повідомлення буде відправлене після натискання кнопки**'))

        async def share_form(interact: Interaction):
            return await interact.response.send_message(
                embed=DefaultEmbed(description='**Це повідомлення буде відправлене після натискання кнопки**'))

        menu_views = MainMenuView(create_form, look_form, delete_form, share_form)
        await interaction.author.send(embed=WelcomePrivateMessage().embed, view=menu_views)

    async def user_age(self, interaction: Interaction):
        await interaction.response.send_message(embed=DefaultEmbed(description='**Скільки тобі років?**'), view=None)

        def check(m):
            if m.channel.id == interaction.channel.id and not m.author.bot:
                return m

        message = await self.client.wait_for('message', check=check)

        try:
            age = int(message.content)
            if age < MIN_AGE or age > MAX_AGE:
                return await interaction.followup.send(embed=DefaultEmbed(description='**Людина вашого віку не може створювати анкету.**'))
            else:
                self.USER_AGE = age
                return await self.call_function(interaction=interaction, function_name='user_gender')
        except ValueError:
            return await interaction.followup.send(embed=DefaultEmbed(description='**Вік введено некоректно.**'))

    async def user_gender(self, interaction: Interaction):
        async def user_chose_gender(interact: Interaction):
            self.USER_GENDER = select_options.values[0]
            return await self.call_function(interaction=interact, function_name='like_gender')

        select_options = Select(custom_id='gender_selection', options=gender_options, placeholder='Оберіть свою стать',
                                min_values=1, max_values=1)

        view = discord.ui.View(timeout=None)
        view.add_item(select_options)

        select_options.callback = user_chose_gender

        await interaction.followup.send(embed=DefaultEmbed(description='**Вкажи свою стать:**'), view=view)

    async def like_gender(self, interaction: Interaction):
        async def user_like_gender(interact: Interaction):
            self.USER_LIKE_GENDER = select_options.values[0]
            return await self.call_function(interaction=interact, function_name='user_location')

        select_options = Select(custom_id='like_gender_selection', options=gender_options, placeholder='Хто тебе цікавить?',
                                min_values=1, max_values=1)

        view = discord.ui.View(timeout=None)
        view.add_item(select_options)

        select_options.callback = user_like_gender

        await interaction.response.send_message(embed=DefaultEmbed(description='**Хто тебе цікавить?**'), view=view)

    async def user_location(self, interaction: Interaction):
        while True:
            try:
                await interaction.response.send_message(embed=DefaultEmbed(description='**З якого ти міста?**'), view=None)
            except discord.errors.InteractionResponded:
                def check(m):
                    if m.channel.id == interaction.channel.id and not m.author.bot:
                        return m

                message = await self.client.wait_for('message', check=check)

                verification_location = check_location(message.content)
                if verification_location is None:
                    await interaction.user.send(embed=DefaultEmbed(description='Локація введена некоректно.\nПовторіть спробу.'))
                    continue
                else:
                    self.USER_LOCATION = message.content
                    return await self.call_function(interaction=interaction, function_name='user_games')

    async def user_games(self, interaction: Interaction):
        await interaction.user.send(embed=DefaultEmbed(description='**Введіть ігри в які ви граєте:**'))

        def check(m):
            if m.channel.id == interaction.channel.id and not m.author.bot:
                return m

        message = await self.client.wait_for('message', check=check)

        if len(message.content) >= 75:
            self.USER_GAMES = message.content[:75]
            return await self.call_function(interaction=interaction, function_name='user_description')
        else:
            self.USER_GAMES = message.content
            return await self.call_function(interaction=interaction, function_name='user_description')

    async def user_description(self, interaction: Interaction):
        await interaction.user.send(embed=DefaultEmbed(description='Введіть опис профілю:'))

        while True:
            def check(m):
                if m.channel.id == interaction.channel.id and not m.author.bot:
                    return m

            message = await self.client.wait_for('message', check=check)

            if len(message.content) > 1024:
                await interaction.user.send(embed=DefaultEmbed(description='Локація введена некоректно.\nПовторіть спробу.'))
                continue
            else:
                self.USER_DESCRIPTION = message.content
                return await self.call_function(interaction=interaction, function_name='user_photo')

    async def user_photo(self, interaction: Interaction):
        await interaction.user.send(embed=DefaultEmbed(description='Загрузіть фото профілю:'))

        while True:
            def check(m):
                if m.channel.id == interaction.channel.id and not m.author.bot:
                    return m

            message = await self.client.wait_for('message', check=check)

            if len(message.attachments) == 0:
                await interaction.followup.send(embed=DefaultEmbed(description='Ви не додали фото профілю. Повторіть спробу.'))
                continue
            self.USER_PHOTO = message.attachments[0]
            return await self.call_function(interaction=interaction, function_name='form_successfully_created')

    async def form_successfully_created(self, interaction: Interaction):
        await interaction.user.send(embed=DefaultEmbed(description='Анкета успішно створена.'))

# todo - продовжити з цього місця, дописати функцію створення анкети користувача та додати user_system.create_user_form
