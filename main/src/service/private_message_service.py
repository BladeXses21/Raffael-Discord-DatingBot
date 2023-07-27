import asyncio

import discord.errors
import requests
from discord import Interaction
from discord.ui import Select

from config import MIN_AGE, MAX_AGE, MIN_NAME_SIZE, MAX_NAME_SIZE
from database.system.user_confirmation import user_confirmed
from database.system.user_form import user_system
from model.user_model.user import UserForm
from templates.embeds.base import DefaultEmbed
from templates.embeds.panelEmbed import MainPanelEmbed

from templates.embeds.user_profile import UserProfileEmbed
from templates.translation_msg.translations import translate_text
from templates.view_builder.accept_button import StartConfirmation
from templates.view_builder.lets_go_button import LetsGoView, OkView
from templates.view_builder.main_view_builder import MainMenuView
from utils.funcs import check_location


class PrivateMessageService:
    """
    This class provides a service for handling private messages from users.

    Attributes:
      # The client that is used to send and receive messages.
      client: Client
      # A dictionary of functions that are used to handle different types of messages.
      function_map: dict
      # A dictionary of functions that have been called.
      function_called: dict
    """
    def __init__(self, client):
        """
        Args:
          # The client that is used to send and receive messages.
          client: Client
        """
        self.client = client
        self.reset_variables()
        self.USER_NAME = str()
        self.USER_AGE = int()
        self.USER_GENDER = str()
        self.OPPOSITE_GENDER = str()
        self.USER_LOCATION = str()
        self.USER_GAMES = str()
        self.USER_DESCRIPTION = str()
        self.USER_PHOTO = str()
        self.USER_LANGUAGE = str()

        self.function_map = {
            'language_scanning': self.language_scanning,
            'presentation_one': self.presentation_one,
            'presentation_two': self.presentation_two,
            'user_name': self.user_name,
            'user_age': self.user_age,
            'user_gender': self.user_gender,
            'opposite_gender': self.opposite_gender,
            'user_location': self.user_location,
            'user_games': self.user_games,
            'user_description': self.user_description,
            'user_photo': self.user_photo,
            'form_successfully_created': self.form_successfully_created,
            'user_profile': self.user_profile,
            'try_again': self.try_again,
        }
        self.function_called = {}

    def reset_variables(self):
        """
        This function resets the class variables to their default values.
        """
        self.USER_NAME = str()
        self.USER_AGE = int()
        self.USER_GENDER = str()
        self.OPPOSITE_GENDER = str()
        self.USER_LOCATION = str()
        self.USER_GAMES = str()
        self.USER_DESCRIPTION = str()
        self.USER_PHOTO = str()
        self.USER_LANGUAGE = str()

    async def call_function(self, interaction: Interaction, function_name: str):
        """
        # This function calls the function with the given name, if it exists.

        # Args:
          # The interaction that triggered the function.
          interaction: Interaction
          # The name of the function to call.
          function_name: str
        """
        if function_name in self.function_map:
            if function_name in self.function_called and self.function_called[function_name]:
                return False

            self.function_called[function_name] = True
            return await self.function_map[function_name](interaction)

    async def language_scanning(self, author):
        """
        # This function sends a message to the user with a button that they can click to continue.
        # it is needed to get the language of the user interface, because without using interaction, it will not be possible to do this
        # Args:
          # The user who triggered the function.
          author: User
        """
        view = StartConfirmation(self.presentation_one)
        return await author.send(embed=DefaultEmbed('**```click on the button to continue```**'), view=view)

    async def presentation_one(self, interaction: Interaction):
        """
        # This function gets the user's language and sends them a message in that language.
        # Sends a text introducing the bot
        # Args:
          # The interaction that triggered the function.
          interaction: Interaction
        """
        user_language = interaction.locale
        self.USER_LANGUAGE = user_language
        lets_go__view = LetsGoView(self.presentation_two, user_language)
        return await interaction.response.send_message(
            embed=DefaultEmbed(f"**```{translate_text('Зараз я допоможу тобі знайти пару або прекрасних друзів', user_language)}```**"),
            view=lets_go__view)

    async def presentation_two(self, interaction: Interaction):
        """
        # This function displays a message to the user in their language, reminding them that there is a possibility of people impersonating themselves online.
        # It also states that the bot does not collect any personal data or identify users through passport or other personal data.

        # Args:
          # The interaction that triggered the function.
          interaction: Interaction
        """
        user_language = interaction.locale
        user_confirmed.user_confirm_rules(interaction.user)
        ok_view = OkView(self.control_panel)
        source_text = translate_text(
            '❗️ Зважаючи на застереження, я хотів би нагадати, що в Інтернеті існує можливість того, що люди можуть представляти себе за когось іншого.\nВарто відзначити, що я, як бот, не збираю жодних особистих даних та не ідентифікую користувачів через паспортні або інші особисті дані. Продовжуючи використовувати бота, ви робите це на свій власний ризик та під свою повну відповідальність.',
            user_language)
        return await interaction.response.send_message(embed=DefaultEmbed(f"**```{source_text}```**"), view=ok_view)

    async def control_panel(self, interaction: Interaction = None, user_data: UserForm = None):
        """
         # This function creates a menu with four buttons: create form, look form, delete form, and share form.
         # If the user_data parameter is not None, the function will send the menu to the user who created the form.
         # Otherwise, the function will send the menu to the user who triggered the function.

         # Args:
           # The interaction that triggered the function, or None if the function was not triggered by an interaction.
           interaction: Interaction
           # The user form data, or None if the function was not triggered by a form.
           user_data: UserForm
         """
        user_language = None
        if interaction is not None:
            user_language = interaction.locale

        async def create_form(interact: Interaction):
            return await self.call_function(interaction=interact, function_name='user_name')

        async def look_form(interact: Interaction):
            return await self.call_function(interaction=interact, function_name='user_profile')

        async def delete_form(interact: Interaction):
            return await interact.response.send_message(
                embed=DefaultEmbed(description=translate_text('Привіт!', user_language)))

        async def share_form(interact: Interaction):
            return await interact.response.send_message(
                embed=DefaultEmbed(description=translate_text('Привіт!', user_language)))

        menu_views = MainMenuView(create_form, look_form, delete_form, share_form)

        if user_data is not None:
            user_dict = UserForm.parse_obj(user_data)
            get_user = await self.client.fetch_user(user_dict.user_id)
            return await get_user.send(embed=MainPanelEmbed(user_dict.language).embed, view=menu_views)
        return await interaction.response.send_message(embed=MainPanelEmbed(user_language).embed, view=menu_views)

    async def user_name(self, interaction: Interaction):
        """
        # This function asks the user to enter their name.
        # The name must be between MIN_NAME_SIZE and MAX_NAME_SIZE characters long.
        # If the name is valid, the function returns the name.
        # Otherwise, the function returns an error message.

        # Args:
          # The interaction that triggered the function.
          interaction: Interaction
        """
        user_language = interaction.locale
        await interaction.user.send(embed=DefaultEmbed(description=translate_text("Введіть ім'я", user_language)), view=None)

        def check(m):
            if m.channel.id == interaction.channel.id and not m.author.bot:
                return m

        message = await self.client.wait_for('message', check=check)

        if len(message.content) >= MAX_NAME_SIZE:
            self.USER_NAME = str(message.content[:30])
            return await self.call_function(interaction=interaction, function_name='user_age')
        else:
            self.USER_NAME = str(message.content)
            return await self.call_function(interaction=interaction, function_name='user_age')

    async def user_age(self, interaction: Interaction):
        """
        # This function asks the user to enter their age.
        # The age must be between MIN_AGE and MAX_AGE.
        # If the age is valid, the function returns the age.
        # Otherwise, the function returns an error message.

        # Args:
          # The interaction that triggered the function.
          interaction: Interaction
        """
        user_language = interaction.locale
        await interaction.user.send(embed=DefaultEmbed(translate_text('Скільки тобі років?', user_language)))

        def check(m):
            if m.channel.id == interaction.channel.id and not m.author.bot:
                return m

        while True:
            msg = await self.client.wait_for('message', check=check)

            try:
                age = int(msg.content)
                if MIN_AGE <= age >= MAX_AGE:
                    self.USER_AGE = int(age)
                    await self.call_function(interaction=interaction, function_name='user_gender')
                    break
                else:
                    raise ValueError
            except ValueError:
                return await interaction.followup.send(embed=DefaultEmbed(description=translate_text('Вік введено некоректно.', user_language)))

    async def user_gender(self, interaction: Interaction):
        """
        # This function asks the user to select their gender.
        # The gender options are "Man", "Woman", and "LGBT".
        # If the user selects a valid gender, the function returns the gender.
        # Otherwise, the function returns an error message.

        # Args:
          # The interaction that triggered the function.
          interaction: Interaction
        """
        user_language = interaction.locale

        async def user_chose_gender(interact: Interaction):
            self.USER_GENDER = select_options.values[0]
            return await self.call_function(interaction=interact, function_name='opposite_gender')

        gender_options = [
            discord.SelectOption(label=translate_text('Хлопець', user_language), value=translate_text('Хлопець', user_language)),
            discord.SelectOption(label=translate_text('Дівчина', user_language), value=translate_text('Дівчина', user_language)),
            discord.SelectOption(label=translate_text('LGBT', user_language), value=translate_text('LGBT', user_language))
        ]

        select_options = Select(custom_id='gender_selection', options=gender_options, placeholder=translate_text('Оберіть свою стать', user_language),
                                min_values=1, max_values=1)

        view = discord.ui.View(timeout=None)
        view.add_item(select_options)

        select_options.callback = user_chose_gender

        await interaction.followup.send(embed=DefaultEmbed(description=translate_text('Вкажи свою стать:', user_language)), view=view)

    async def opposite_gender(self, interaction: Interaction):
        """
        # This function asks the user to select opposite gender.
        # The gender options are "Man", "Woman", and "LGBT".
        # If the user selects a valid gender, the function returns the gender.
        # Otherwise, the function returns an error message.

        # Args:
          # The interaction that triggered the function.
          interaction: Interaction
        """
        user_language = interaction.locale

        async def user_like_gender(interact: Interaction):
            """
            # This function is called when the user selects an option from the SelectView.
            # It stores the selected option in the `OPPOSITE_GENDER` attribute and returns.
            """
            self.OPPOSITE_GENDER = select_options.values[0]
            return await self.call_function(interaction=interact, function_name='user_location')

        gender_options = [
            discord.SelectOption(label=translate_text("Хлопець", user_language),
                                 value=translate_text("Хлопець", user_language)),
            discord.SelectOption(label=translate_text("Дівчина", user_language),
                                 value=translate_text("Дівчина", user_language)),
            discord.SelectOption(label=translate_text("LGBT", user_language),
                                 value=translate_text("LGBT", user_language))
        ]
        select_options = Select(custom_id='like_gender_selection', options=gender_options,
                                placeholder=translate_text('Хто тебе цікавить?', user_language),
                                min_values=1, max_values=1)

        view = discord.ui.View(timeout=None)
        view.add_item(select_options)

        select_options.callback = user_like_gender

        await interaction.response.send_message(embed=DefaultEmbed(description=translate_text('Хто тебе цікавить?', user_language)), view=view)

    async def user_location(self, interaction: Interaction):
        """
        # This function asks the user to enter their city.
        # If the user enters a valid city, the function returns the city.
        # Otherwise, the function returns an error message.

        # Args:
          # The interaction that triggered the function.
          interaction: Interaction
        """

        user_language = interaction.locale
        lock = asyncio.Lock()

        async with lock:
            while True:
                try:
                    await interaction.response.send_message(embed=DefaultEmbed(description=translate_text('З якого ти міста?', user_language)),
                                                            view=None)
                except discord.errors.InteractionResponded:
                    def check(m):
                        if m.channel.id == interaction.channel.id and not m.author.bot:
                            return m

                    message = await self.client.wait_for('message', check=check)

                    verification_location = check_location(message.content)
                    if verification_location is None:
                        await interaction.user.send(
                            embed=DefaultEmbed(description=translate_text('Локація введена некоректно.\nПовторіть спробу.', user_language)))
                        continue
                    else:
                        self.USER_LOCATION = message.content
                        return await self.call_function(interaction=interaction, function_name='user_games')

    async def user_games(self, interaction: Interaction):
        """
        # This function asks the user to enter their favorite games.
        # If the user enters valid games, the function returns the games.
        # Otherwise, the function returns an error message.

        # Args:
          # The interaction that triggered the function.
          interaction: Interaction
        """
        user_language = interaction.locale
        await interaction.user.send(embed=DefaultEmbed(description=translate_text('Введіть ігри в які ви граєте:', user_language)))

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
        """
        This function asks the user to enter a description for their profile.
        The description must be less than 1024 characters long.
        If the user enters a valid description, the function returns the description.
        Otherwise, the function returns an error message.

        Args:
          # The interaction that triggered the function.
          interaction: Interaction
        """
        user_language = interaction.locale
        await interaction.user.send(embed=DefaultEmbed(description=translate_text('Введіть опис профілю:', user_language)))

        while True:
            def check(m):
                if m.channel.id == interaction.channel.id and not m.author.bot:
                    return m

            message = await self.client.wait_for('message', check=check)

            if len(message.content) > 1024:
                await interaction.user.send(embed=DefaultEmbed(description=translate_text('Текст занадто великий, повторіть спробу:', user_language)))
                continue
            else:
                self.USER_DESCRIPTION = message.content
                print(self.USER_DESCRIPTION)
                return await self.call_function(interaction=interaction, function_name='user_photo')

    async def user_photo(self, interaction: Interaction):
        """
        This function asks the user to upload a photo for their profile.
        The photo must be a valid image file.
        If the user uploads a valid photo, the function returns the photo's URL.
        Otherwise, the function returns an error message.

        Args:
          # The interaction that triggered the function.
          interaction: Interaction
        """
        user_language = interaction.locale
        lock = asyncio.Lock()
        await interaction.user.send(embed=DefaultEmbed(description=translate_text('Загрузіть фото профілю:', user_language)))

        async with lock:
            while True:
                def check(m):
                    if m.channel.id == interaction.channel.id and not m.author.bot:
                        return m

                message = await self.client.wait_for('message', check=check)
                attachment_url = str(message.attachments[0])

                if len(message.attachments) == 0:
                    await interaction.followup.send(
                        embed=DefaultEmbed(description=translate_text('Ви не додали фото профілю. Повторіть спробу.', user_language)))
                    continue
                if not self.is_valid_image_url(attachment_url):
                    await interaction.followup.send(
                        embed=DefaultEmbed(description=translate_text('Ви додали невірне посилання на зображення. Повторіть спробу.', user_language)))
                    continue

                self.USER_PHOTO = str(message.attachments[0])
                print(self.USER_PHOTO)
                return await self.call_function(interaction=interaction, function_name='form_successfully_created')

    async def form_successfully_created(self, interaction: Interaction):
        """
        Sends a message to the user confirming that their form has been created successfully.

        Args:
          interaction: The interaction that triggered the function.
        """

        user_language = interaction.locale
        user_system.create_user_form(id=interaction.user.id, name=self.USER_NAME, age=self.USER_AGE, gender=self.USER_GENDER,
                                     opposite_gender=self.OPPOSITE_GENDER, location=self.USER_LOCATION, games=self.USER_GAMES,
                                     description=self.USER_DESCRIPTION, photo=self.USER_PHOTO, language=user_language)
        await interaction.user.send(embed=DefaultEmbed(description=translate_text('Анкета успішно створена.', user_language)))
        self.reset_variables()
        self.function_called = {}
        return await self.call_function(interaction=interaction, function_name='user_profile')

    async def user_profile(self, interaction: Interaction):
        """
        This function fetches the user's profile data from the database and sends it to the user in an embed.

        Args:
          # The interaction that triggered the function.
          interaction: Interaction
        """
        user = interaction.user
        fetch_user = user_system.fetch_variables_by_user(user=user)
        print(fetch_user)
        if fetch_user is not False:
            return await interaction.user.send(embed=UserProfileEmbed(fetch_user).embed)
        else:
            return await self.call_function(interaction=interaction, function_name='try_again')

    async def try_again(self, interaction: Interaction):
        """
        This function sends a message to the user asking them if they want to try again to create their profile.

        Args:
          # The interaction that triggered the function.
          interaction: Interaction
        """
        user_language = interaction.locale

        return await interaction.user.send(embed=DefaultEmbed(
            description=translate_text('Відбулась помилка реєстрації анкети, бажаєте повторити спробу створення анкети?', user_language)))

    @staticmethod
    def is_valid_image_url(url):
        """
        This function checks if the given URL is a valid image URL.

        Args:
          # The URL to check.
          url: str

        Returns:
          # True if the URL is a valid image URL, False otherwise.
          bool
        """
        try:
            response = requests.head(url)
            if response.status_code == 200 and response.headers.get('content-type', '').startswith('image/'):
                return True
            return False
        except requests.RequestException:
            return False
