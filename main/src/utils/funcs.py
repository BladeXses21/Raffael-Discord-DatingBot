from geopy.geocoders import Nominatim
import cv2


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


def check_photo_validity(photo):
    photo = cv2.imread(photo)

    if photo is None:
        # помилка завантаження фото
        return False
    return True
