import discord.errors
from discord import Interaction

from config import MIN_AGE, MAX_AGE
from embed.embeds.base import DefaultEmbed
from embed.embeds.welcome import WelcomePrivateMessage
from embed.view_builder.chose_gender_builder import ChoseGenderView
from embed.view_builder.like_gender_builder import ChoseLikeGender
from embed.view_builder.main_view_builder import MainMenuView
from extension.logger import logger
from utils.funcs import check_location


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

    async def mainMenu(self, interaction):
        logger.info(f'{interaction.author.id} | {interaction.author} викликав mainMenu')

        async def create_form(interact: Interaction):
            return await self.user_age(interact)

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
                await self.user_gender(interaction)
        except ValueError:
            return await interaction.followup.send(embed=DefaultEmbed(description='**Вік введено некоректно.**'))

    async def user_gender(self, interaction: Interaction):

        async def user_is_woman(interact: Interaction):
            self.USER_GENDER = 'woman'
            return await self.like_gender(interact)

        async def user_is_man(interact: Interaction):
            self.USER_GENDER = 'man'
            return await self.like_gender(interact)

        # gender_views = ChoseGenderView(user_is_woman, user_is_man)

        gender_options = [
            discord.SelectOption(label='Хлопець', value='man'),
            discord.SelectOption(label='Дівчина', value='woman'),
            discord.SelectOption(label='ЛГБТ-клуб', value='lgbt')
        ]

        select_options = discord.SelectMenu(custom_id='gender_selection', options=gender_options, placeholder='Оберіть свою стать',
                                            min_values=1, max_values=1)

        await interaction.followup.send(embed=DefaultEmbed(description='**Вкажи свою стать:**'), view=select_options)

    async def like_gender(self, interaction: Interaction):

        async def user_like_woman(interact: Interaction):
            self.USER_LIKE_GENDER = 'woman'
            await self.user_location(interact)

        async def user_like_man(interact: Interaction):
            self.USER_LIKE_GENDER = 'man'
            await self.user_location(interact)

        like_gender_view = ChoseLikeGender(user_like_woman, user_like_man)

        await interaction.response.send_message(embed=DefaultEmbed(description='**Хто тебе цікавить?**'), view=like_gender_view)

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
                    await self.user_games(interaction)
                    break

    async def user_games(self, interaction: Interaction):
        await interaction.user.send(embed=DefaultEmbed(description='**Введіть ігри в які ви граєте:**'))

        def check(m):
            if m.channel.id == interaction.channel.id and not m.author.bot:
                return m

        message = await self.client.wait_for('message', check=check)

        if len(message.content) >= 75:
            self.USER_GAMES = message.content[:75]
            await self.user_description(interaction)
        else:
            self.USER_GAMES = message.content
            await self.user_description(interaction)

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
                await self.user_photo(interaction)
                break

    async def user_photo(self, interaction: Interaction):
        print(self.USER_DESCRIPTION, self.USER_LOCATION, self.USER_LIKE_GENDER, self.USER_GENDER)
        await interaction.user.send(embed=DefaultEmbed(description='Загрузіть фото профілю:'))

        while True:
            def check(m):
                if m.channel.id == interaction.channel.id and not m.author.bot:
                    return m

            message = await self.client.wait_for('message', check=check)

            if len(message.attachments) == 0:
                await interaction.followup.send(embed=DefaultEmbed(description='Ви не додали фото профілю. Повторіть спробу.'))
                continue
            attachment_url = message.attachments[0]
            await interaction.followup.send(embed=DefaultEmbed(description='Ви надіслали фото профілю!'))
            break
