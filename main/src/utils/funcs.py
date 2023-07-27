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
    if not user_form.location or user_form.location is int():
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
