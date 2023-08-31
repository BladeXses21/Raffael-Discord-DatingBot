import discord
from discord import Interaction
from discord.ui import InputText, Modal

from database.system.user_form import user_system
from templates.embeds.base import DefaultEmbed
from templates.localization.translations import translate_text
from utils.funcs import check_location


class EditNameModal(Modal):
    def __init__(self, interaction: Interaction):
        super().__init__(title=translate_text('fill_form', language=interaction.locale))
        self.interaction = interaction
        user_language = interaction.locale
        self.add_item(InputText(style=discord.InputTextStyle.short, label=translate_text('enter_name', language=user_language)))

    async def callback(self, interaction: discord.Interaction):
        user_system.update_user_field(user_id=interaction.user.id, field_name='name', new_value=self.children[0].value)
        try:
            return await interaction.response.send_message(embed=DefaultEmbed(description=self.children[0].value), ephemeral=True)
        except discord.interactions.InteractionResponse:
            return await interaction.user.send(embed=DefaultEmbed(description=self.children[0].value))


class EditAgeModal(Modal):
    def __init__(self, interaction: Interaction):
        super().__init__(title=translate_text('fill_form', language=interaction.locale))
        self.interaction = interaction
        user_language = interaction.locale
        self.add_item(InputText(style=discord.InputTextStyle.short, label=translate_text('how_old', language=user_language)))

    async def callback(self, interaction: discord.Interaction):
        user_system.update_user_field(user_id=interaction.user.id, field_name='age', new_value=self.children[0].value)
        try:
            return await interaction.response.send_message(embed=DefaultEmbed(description=self.children[0].value), ephemeral=True)
        except discord.interactions.InteractionResponse:
            return await interaction.user.send(embed=DefaultEmbed(description=self.children[0].value))


class EditLocationModal(Modal):
    def __init__(self, interaction: Interaction):
        super().__init__(title=translate_text('fill_form', language=interaction.locale))
        self.interaction = interaction
        user_language = interaction.locale
        self.add_item(InputText(style=discord.InputTextStyle.short, label=translate_text('your_city', language=user_language)))

    async def callback(self, interaction: discord.Interaction):
        latitude, longitude = check_location(self.children[0].value)
        if latitude is None:
            return await interaction.user.send(embed=DefaultEmbed(description=translate_text('location_error', interaction.locale)))
        user_location = []
        user_location.extend([latitude, longitude])
        user_system.update_user_field(user_id=interaction.user.id, field_name='location', new_value=user_location)
        try:
            return await interaction.response.send_message(embed=DefaultEmbed(description=self.children[0].value), ephemeral=True)
        except discord.interactions.InteractionResponse:
            return await interaction.user.send(embed=DefaultEmbed(description=self.children[0].value))


class EditGameModal(Modal):
    def __init__(self, interaction: Interaction):
        super().__init__(title=translate_text('fill_form', language=interaction.locale))
        self.interaction = interaction
        user_language = interaction.locale
        self.add_item(InputText(style=discord.InputTextStyle.short, label=translate_text('enter_games', language=user_language)))

    async def callback(self, interaction: discord.Interaction):
        user_system.update_user_field(user_id=interaction.user.id, field_name='games', new_value=self.children[0].value)
        try:
            return await interaction.response.send_message(embed=DefaultEmbed(description=self.children[0].value), ephemeral=True)
        except discord.interactions.InteractionResponse:
            return await interaction.user.send(embed=DefaultEmbed(description=self.children[0].value))


class EditDescriptionModal(Modal):
    def __init__(self, interaction: Interaction):
        super().__init__(title=translate_text('fill_form', language=interaction.locale))
        self.interaction = interaction
        user_language = interaction.locale
        self.add_item(InputText(style=discord.InputTextStyle.long, label=translate_text('profile_description', language=user_language)))

    async def callback(self, interaction: discord.Interaction):
        user_system.update_user_field(user_id=interaction.user.id, field_name='description', new_value=self.children[0].value)
        try:
            return await interaction.response.send_message(embed=DefaultEmbed(description=self.children[0].value), ephemeral=True)
        except discord.interactions.InteractionResponse:
            return await interaction.user.send(embed=DefaultEmbed(description=self.children[0].value))

# todo - добавити до класів перевірку даних як при реєстрації.
