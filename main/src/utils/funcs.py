from geopy.geocoders import Nominatim


def check_location(location):
    if location.isdigit():
        return None
    elif any(char.isdigit() for char in location):
        return None
    try:
        geolocator = Nominatim(user_agent='CupidBot')
        location = geolocator.geocode(str(location))
    except TimeoutError:
        return None
    return location
