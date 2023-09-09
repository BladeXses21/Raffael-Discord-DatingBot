import json
from math import pi

from discord import Embed, Interaction
from geopy.geocoders import Nominatim
import geopy.distance
import requests

from config import OPENCAGEDATA_API_KEY
from database.system.user_form import user_system
from model.user_model.user import UserForm
from templates.embeds.base import DefaultEmbed
from templates.localization.translations import translate_text


def get_embed(json_):
    embed_json = json.loads(json_)

    embed = Embed().from_dict(embed_json)
    return embed


def is_valid_image_url(url) -> bool:
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


def get_city_from_coordinates(latitude, longitude):
    url = f"https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=json"
    response = requests.get(url)
    data = response.json()
    # Перелік можливих ключів адреси
    address_keys = ['town', 'city', 'village', 'suburb', 'hamlet', 'locality']

    for key in address_keys:
        if 'address' in data:
            value = data['address'].get(key, '')
            if value:
                return value
    return ''


def check_location(location):
    url = f'https://api.opencagedata.com/geocode/v1/json?q={location}&key={OPENCAGEDATA_API_KEY}'

    try:
        # Виконуємо GET-запит до API.
        response = requests.get(url)

        # Перевіряємо, чи отримали ми успішну відповідь від сервера.
        if response.status_code == 200:
            data = response.json()

            # Парсимо дані, щоб отримати координати.
            if 'results' in data and len(data['results']) > 0:
                lat = data['results'][0]['geometry']['lat']
                lon = data['results'][0]['geometry']['lng']
                print(lat, lon)
                return lat, lon
            else:
                return None
        else:
            print('Помилка під час виконання запиту:', response.status_code)
            return None
    except Exception as e:
        print('Помилка:', str(e))
        return None


# validate user form in user_form system

def validate_user_form(user_form):
    if not user_form.user_id or user_form.user_id is str():
        return False
    if not user_form.name or user_form.name is int():
        return False
    if not user_form.age or user_form.age is str():
        return False
    if not user_form.gender or user_form.gender is int():
        return False
    if not user_form.opposite_gender or user_form.opposite_gender is int():
        return False
    if not user_form.location or user_form.location is list():
        return False
    if not user_form.games or user_form.games is int():
        return False
    if not user_form.description or user_form.description is int():
        return False
    if not user_form.photo or user_form.photo is int():
        return False
    if not user_form.language or user_form.language is int():
        return False
    return True


# todo - передивитись цю функцію для пошуку анкет

def search_users(user_location, radius, all_users):
    """Searches for users who are within a given radius of the user's location.

    Args:
      user_location: The user's location, as a tuple of (latitude, longitude).
      radius: The search radius, in kilometers.
      all_users: A list of all users with their locations.

    Returns:
      A list of users who are within the search radius.
    """
    # Filter the users by location.
    filtered_users = [
        UserForm.parse_obj(user) for user in all_users if
        distance_between_points(user_location[0], user_location[1], user.location[0], user.location[1]) <= radius
    ]
    # Return the filtered list of users.
    return filtered_users


def distance_between_points(lat1, lon1, lat2, lon2):
    """Calculates the distance between two points.

    Args:
      lat1: The latitude of the first point.
      lon1: The longitude of the first point.
      lat2: The latitude of the second point.
      lon2: The longitude of the second point.

    Returns:
      The distance between the two points, in kilometers.
    """

    # Calculate the distance between the two points.
    distance = geopy.distance.geodesic((lat1, lon1), (lat2, lon2)).kilometers

    # Return the distance.
    return distance
