import asyncio

import discord.errors
from discord import Interaction

from config import MIN_AGE, MAX_AGE, MAX_NAME_SIZE
from database.system.user_confirmation import user_confirmed
from database.system.user_form import user_system
from model.user_model.user import UserForm
from templates.embeds.base import DefaultEmbed
from templates.embeds.mainPanel import MainPanelEmbed
from templates.embeds.settingsPanel import SettingsEmbed

from templates.embeds.userProfile import UserProfileEmbed
from templates.localization.translations import translate_text
from templates.modal_window.edit_modal_builder import EditDescriptionModal, EditGameModal, EditLocationModal, EditAgeModal, EditNameModal
from templates.views.accept_view_builder import StartConfirmation
from templates.views.gender_select_builder import GenderSelectView
from templates.views.lets_go_view_builder import LetsGoView, OkView
from templates.views.main_view_builder import MainMenuView
from templates.views.settings_view_builder import SettingsMenuView
from utils.funcs import check_location, is_valid_image_url


class PrivateMessageService:
    """
    This class provides a service for handling private messages from users.

    Attributes:
      # The client that is used to send and receive messages.
      client: Client
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
        self.USER_LOCATION = []
        self.USER_GAMES = str()
        self.USER_DESCRIPTION = str()
        self.USER_PHOTO = str()
        self.USER_LANGUAGE = str()

    def reset_variables(self):
        """
        This function resets the class variables to their default values.
        """
        self.USER_NAME = str()
        self.USER_AGE = int()
        self.USER_GENDER = str()
        self.OPPOSITE_GENDER = str()
        self.USER_LOCATION = []
        self.USER_GAMES = str()
        self.USER_DESCRIPTION = str()
        self.USER_PHOTO = str()
        self.USER_LANGUAGE = str()

    async def language_scanning(self, author):
        """
        # This function sends a message to the user with a button that they can click to continue.
        # it is needed to get the language of the user interface, because without using interaction, it will not be possible to do this
        # Args:
          # The user who triggered the function.
          author: User
        """

        def start_presentation(interact: Interaction):
            return self.presentation_one(interact)

        view = StartConfirmation(start_presentation, language='en')
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

        def continued_presentation(interact: Interaction):
            return self.presentation_two(interact)

        lets_go__view = LetsGoView(continued_presentation, user_language)
        try:
            return await interaction.response.send_message(embed=DefaultEmbed(f"**```{translate_text('start_message', user_language)}```**"),
                                                           view=lets_go__view)
        except discord.errors.InteractionResponded:
            return await interaction.user.send(embed=DefaultEmbed(f"**```{translate_text('start_message', user_language)}```**"), view=lets_go__view)

    async def presentation_two(self, interaction: Interaction):
        """
        # This function displays a message to the user in their language, reminding them that there is a possibility of people impersonating
        themselves online. # It also states that the bot does not collect any personal data or identify users through passport or other personal data.

        # Args:
          # The interaction that triggered the function.
          interaction: Interaction
        """
        user_language = interaction.locale

        def confirmation_presentation(interact: Interaction):
            user_confirmed.user_confirm_rules(interaction.user)
            return self.control_panel(interact)

        ok_view = OkView(confirmation_presentation)
        source_text = translate_text('disclaimer', user_language)
        try:
            return await interaction.response.send_message(embed=DefaultEmbed(f"**```{source_text}```**"), view=ok_view)
        except discord.errors.InteractionResponded:
            await interaction.user.send(embed=DefaultEmbed(f"**```{source_text}```**"), view=ok_view)

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
        user_language = 'en'
        if interaction is not None:
            user_language = interaction.locale

        async def share_form(interact: Interaction):
            # todo - прибрати з часом
            return await interact.response.send_message(embed=DefaultEmbed(description=translate_text('greeting', user_language)))

        menu_views = MainMenuView(share_form=share_form)

        if user_data is not None:
            user_dict = UserForm.parse_obj(user_data)
            get_user = await self.client.fetch_user(user_dict.user_id)
            return await get_user.send(embed=MainPanelEmbed(user_dict.language).embed, view=menu_views)

        if interaction.message is None:
            try:
                await interaction.response.send_message(embed=MainPanelEmbed(user_language).embed, view=menu_views)
            except discord.errors.InteractionResponded:
                await interaction.user.send(embed=MainPanelEmbed(user_language).embed, view=menu_views)
        else:
            await interaction.response.edit_message(embed=MainPanelEmbed(user_language).embed, view=menu_views)

    async def user_settings(self, interaction: Interaction):
        user = interaction.user
        fetch_user = user_system.fetch_variables_by_user(user=user)
        if fetch_user is False:
            await self.try_again(interaction)
            return self.user_name(interaction)

        user_language = interaction.locale

        settings_view = SettingsMenuView(
            name=self.edit_name,
            age=self.edit_age,
            gender=self.edit_gender,
            opposite_gender=self.edit_opposite_gender,
            location=self.edit_location,
            games=self.edit_games,
            description=self.edit_description,
            photo=self.edit_photo,
            back=self.back_to_menu,
        )

        if interaction.message is None:
            await interaction.response.send_message(embed=SettingsEmbed(user_language).embed, view=settings_view)
        else:
            await interaction.response.edit_message(embed=SettingsEmbed(user_language).embed, view=settings_view)

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
        view = discord.ui.View()
        try:
            await interaction.response.send_message(embed=DefaultEmbed(translate_text("enter_name", user_language)), view=view)
        except discord.errors.InteractionResponded:
            await interaction.user.send(embed=DefaultEmbed(translate_text("enter_name", user_language)), view=view)

        def check(m):
            if m.channel.id == interaction.channel.id and not m.author.bot:
                return m

        message = await self.client.wait_for('message', check=check)

        if len(message.content) >= MAX_NAME_SIZE:
            self.USER_NAME = str(message.content[:30])
            return await self.user_age(interaction)
        else:
            self.USER_NAME = str(message.content)
            return await self.user_age(interaction)

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
        try:
            await interaction.response.send_message(embed=DefaultEmbed(translate_text('how_old', user_language)))
        except discord.errors.InteractionResponded:
            await interaction.user.send(embed=DefaultEmbed(translate_text('how_old', user_language)))

        def check(m):
            if m.channel.id == interaction.channel.id and not m.author.bot:
                return m

        while True:
            msg = await self.client.wait_for('message', check=check)

            try:
                age = int(msg.content)
                if MIN_AGE <= age <= MAX_AGE:
                    self.USER_AGE = int(age)
                    return await self.user_gender(interaction)
                else:
                    raise ValueError
            except ValueError:
                await interaction.followup.send(embed=DefaultEmbed(description=translate_text('age_error', user_language)))
                return self.user_age(interaction)

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
            self.USER_GENDER = select_view.values[0]
            return await self.opposite_gender(interact)

        select_view = GenderSelectView(
            user_language=user_language,
            callback=user_chose_gender,
            placeholder=translate_text('choose_gender', user_language)
        )

        view = discord.ui.View(timeout=None)
        view.add_item(select_view)

        try:
            return await interaction.response.send_message(embed=DefaultEmbed(description=translate_text('choose_gender_hint', user_language)),
                                                           view=view)
        except discord.errors.InteractionResponded:
            return await interaction.user.send(embed=DefaultEmbed(description=translate_text('choose_gender_hint', user_language)), view=view)

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
            self.OPPOSITE_GENDER = select_view.values[0]
            return await self.user_location(interact)

        select_view = GenderSelectView(
            user_language=user_language,
            callback=user_like_gender,
            placeholder=translate_text('choose_gender', user_language)
        )
        view = discord.ui.View(timeout=None)
        view.add_item(select_view)

        try:
            return await interaction.response.send_message(embed=DefaultEmbed(description=translate_text('interested_in', user_language)), view=view)
        except discord.errors.InteractionResponded:
            return await interaction.user.send(embed=DefaultEmbed(description=translate_text('interested_in', user_language)), view=view)

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
        view = discord.ui.View()
        try:
            await interaction.response.send_message(embed=DefaultEmbed(description=translate_text('your_city', user_language)), view=view)
        except discord.errors.InteractionResponded:
            await interaction.user.send(embed=DefaultEmbed(description=translate_text('your_city', user_language)), view=view)

        async with lock:
            while True:
                def check(m):
                    if m.channel.id == interaction.channel.id and not m.author.bot:
                        return m

                message = await self.client.wait_for('message', check=check)
                latitude, longitude = check_location(message.content)
                if latitude is None:
                    await interaction.user.send(embed=DefaultEmbed(description=translate_text('location_error', user_language)))
                    continue
                else:
                    self.USER_LOCATION.extend([latitude, longitude])
                    return await self.user_games(interaction)

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
        try:
            await interaction.response.send_message(embed=DefaultEmbed(description=translate_text('enter_games', user_language)))
        except discord.errors.InteractionResponded:
            await interaction.user.send(embed=DefaultEmbed(description=translate_text('enter_games', user_language)))

        def check(m):
            if m.channel.id == interaction.channel.id and not m.author.bot:
                return m

        message = await self.client.wait_for('message', check=check)

        if len(message.content) >= 75:
            self.USER_GAMES = message.content[:75]
            return await self.user_description(interaction)
        else:
            self.USER_GAMES = message.content
            return await self.user_description(interaction)

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
        try:
            await interaction.response.send_message(embed=DefaultEmbed(description=translate_text('profile_description', user_language)))
        except discord.errors.InteractionResponded:
            await interaction.user.send(embed=DefaultEmbed(description=translate_text('profile_description', user_language)))

        while True:
            def check(m):
                if m.channel.id == interaction.channel.id and not m.author.bot:
                    return m

            message = await self.client.wait_for('message', check=check)

            if len(message.content) > 1024:
                try:
                    await interaction.response.send_message(embed=DefaultEmbed(description=translate_text('text_too_large', user_language)))
                except discord.errors.InteractionResponded:
                    await interaction.user.send(embed=DefaultEmbed(description=translate_text('text_too_large', user_language)))
                continue
            else:
                self.USER_DESCRIPTION = message.content
                return await self.user_photo(interaction)

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
        try:
            await interaction.response.send_message(embed=DefaultEmbed(description=translate_text('upload_photo', user_language)))
        except discord.errors.InteractionResponded:
            await interaction.user.send(embed=DefaultEmbed(description=translate_text('upload_photo', user_language)))

        async with lock:
            while True:
                def check(m):
                    if m.channel.id == interaction.channel.id and not m.author.bot:
                        return m

                message = await self.client.wait_for('message', check=check)
                attachment_url = str(message.attachments[0])

                if len(message.attachments) == 0:
                    await interaction.followup.send(embed=DefaultEmbed(description=translate_text('no_photo_error', user_language)))
                    continue
                if not is_valid_image_url(attachment_url):
                    await interaction.followup.send(embed=DefaultEmbed(description=translate_text('no_photo_url_error', user_language)))
                    continue

                self.USER_PHOTO = str(message.attachments[0])
                return await self.form_successfully_created(interaction)

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
        try:
            await interaction.response.send_message(embed=DefaultEmbed(description=translate_text('form_success', user_language)))
        except discord.errors.InteractionResponded:
            await interaction.user.send(embed=DefaultEmbed(description=translate_text('form_success', user_language)))
        self.reset_variables()
        return await self.user_profile(interaction)

    async def user_profile(self, interaction: Interaction):
        """
        This function fetches the user's profile data from the database and sends it to the user in an embed.

        Args:
          # The interaction that triggered the function.
          interaction: Interaction
        """
        user = interaction.user
        fetch_user = user_system.fetch_variables_by_user(user=user)

        if fetch_user is not False:
            try:
                return await interaction.response.send_message(embed=UserProfileEmbed(fetch_user).embed)
            except discord.errors.InteractionResponded:
                await interaction.user.send(embed=UserProfileEmbed(fetch_user).embed)
        else:
            return await self.try_again(interaction)

    async def back_to_menu(self, interaction: Interaction):
        return await self.control_panel(interaction)

    async def try_again(self, interaction: Interaction):
        """
        This function sends a message to the user asking them if they want to try again to create their profile.

        Args:
          # The interaction that triggered the function.
          interaction: Interaction
        """
        user_language = interaction.locale
        try:
            return await interaction.response.send_message(embed=DefaultEmbed(description=translate_text('try_again', user_language)))
        except discord.errors.InteractionResponded:
            return await interaction.user.send(embed=DefaultEmbed(description=translate_text('try_again', user_language)))

    @staticmethod
    async def edit_name(interaction: Interaction):
        staff_modal = EditNameModal(interaction)
        await interaction.response.send_modal(modal=staff_modal)

    @staticmethod
    async def edit_age(interaction: Interaction):
        staff_modal = EditAgeModal(interaction)
        await interaction.response.send_modal(modal=staff_modal)

    @staticmethod
    async def edit_location(interaction: Interaction):
        staff_modal = EditLocationModal(interaction)
        await interaction.response.send_modal(modal=staff_modal)

    @staticmethod
    async def edit_games(interaction: Interaction):
        staff_modal = EditGameModal(interaction)
        await interaction.response.send_modal(modal=staff_modal)

    @staticmethod
    async def edit_description(interaction: Interaction):
        staff_modal = EditDescriptionModal(interaction)
        await interaction.response.send_modal(modal=staff_modal)

    @staticmethod
    async def edit_gender(interaction: Interaction):
        async def chose_gender(interact: Interaction):
            user_system.update_user_field(user_id=interaction.user.id, field_name='gender', new_value=select_view.values[0])
            return await interact.response.edit_message(select_view.values[0])

        user_language = interaction.locale
        select_view = GenderSelectView(
            user_language=user_language,
            callback=chose_gender,
            placeholder=translate_text('choose_gender', user_language)
        )

        view = discord.ui.View(timeout=None)
        view.add_item(select_view)
        await interaction.response.send_message(embed=DefaultEmbed(description=translate_text('choose_gender_hint', user_language)), view=view,
                                                ephemeral=True)

    @staticmethod
    async def edit_opposite_gender(interaction: Interaction):
        async def chose_opposite_gender(interact: Interaction):
            user_system.update_user_field(user_id=interaction.user.id, field_name='opposite_gender', new_value=select_view.values[0])
            return await interact.response.edit_message(select_view.values[0])

        user_language = interaction.locale
        select_view = GenderSelectView(
            user_language=user_language,
            callback=chose_opposite_gender,
            placeholder=translate_text('choose_gender', user_language)
        )

        view = discord.ui.View(timeout=None)
        view.add_item(select_view)

        await interaction.response.send_message(embed=DefaultEmbed(description=translate_text('interested_in', user_language)), view=select_view,
                                                ephemeral=True)

    async def edit_photo(self, interaction: Interaction):
        user_language = interaction.locale
        lock = asyncio.Lock()
        try:
            await interaction.response.send_message(embed=DefaultEmbed(description=translate_text('upload_photo', user_language)), ephemeral=True)
        except discord.errors.InteractionResponded:
            await interaction.user.send(embed=DefaultEmbed(description=translate_text('upload_photo', user_language)))

        async with lock:
            while True:
                def check(m):
                    if m.channel.id == interaction.channel.id and not m.author.bot:
                        return m

                message = await self.client.wait_for('message', check=check)
                attachment_url = str(message.attachments[0])

                if len(message.attachments) == 0:
                    try:
                        await interaction.response.send_message(embed=DefaultEmbed(description=translate_text('no_photo_error', user_language)))
                    except discord.errors.InteractionResponded:
                        await interaction.user.send(embed=DefaultEmbed(description=translate_text('no_photo_error', user_language)))
                    continue
                if not is_valid_image_url(attachment_url):
                    try:
                        await interaction.response.send_message(embed=DefaultEmbed(description=translate_text('no_photo_url_error', user_language)))
                    except discord.errors.InteractionResponded:
                        await interaction.user.send(embed=DefaultEmbed(description=translate_text('no_photo_url_error', user_language)))
                    continue

                user_system.update_user_field(user_id=interaction.user.id, field_name='photo', new_value=str(message.attachments[0]))
                # todo - добавити до локалізації
                return await interaction.edit_original_response(embed=DefaultEmbed(description="Фото успішно оновлено"))
