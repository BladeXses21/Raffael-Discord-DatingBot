import discord
from geopy.geocoders import Nominatim
import geopy.distance


def check_location(location):
    """
    Check if a location is valid.

    Args:
      location: The location to check.

    Returns:
      True if the location is valid, False otherwise.
    """
    if location.isdigit():
        return None
    elif any(char.isdigit() for char in location):
        return None
    try:
        geolocator = Nominatim(user_agent='Raffael')
        location = geolocator.geocode(str(location))
    except TimeoutError:
        return None
    return location.latitude, location.longitude


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

def search_users(user_location, radius):
    """Searches for users who are within a given radius of the user's location.

    Args:
      user_location: The user's location, as a tuple of (latitude, longitude).
      radius: The search radius, in kilometers.

    Returns:
      A list of users who are within the search radius.
    """

    # Get the list of all users.
    users = get_all_users()

    # Filter the users by location.
    filtered_users = [user for user in users if distance_between_points(user_location, user.location) <= radius]

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

    # Convert the latitude and longitude values to radians.
    lat1 = lat1 * pi / 180
    lon1 = lon1 * pi / 180
    lat2 = lat2 * pi / 180
    lon2 = lon2 * pi / 180

    # Calculate the distance between the two points.
    distance = geopy.distance.distance(
        (lat1, lon1),
        (lat2, lon2),
        unit='km'
    ).km

    # Return the distance.
    return distance
