# translate in such languages: uk, en, ru, de, fr, es, it, pl, ja, zh, ko

# todo - потрібно добавити такі мови як - el, la, vi, th, ar, he та після потрібно видалити російську


import os
import json

from model.user_model.user import UserForm


def load_localization(language):
    localization_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(localization_folder, f'{language}.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return None


# todo - панель керування зробити велики літерами у всіх локалізаціях
def translate_text(text, language):
    localization = load_localization(language)
    if text in localization[language]:
        return localization[language][text]
    else:
        localization_en = load_localization('en')
        if text in localization_en['en']:
            return localization_en['en'][text]
        return text


def get_gender_emoji(user_gender: str) -> str:
    match user_gender:
        case "boy":
            return "♂"
        case "girl":
            return "♀"
        case "lgbt":
            return "🌈"
        case _:
            return ""
