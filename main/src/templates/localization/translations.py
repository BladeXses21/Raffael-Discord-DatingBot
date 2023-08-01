# translate in such languages: uk, en, ru, de, fr, es, it, pl, ja, zh, ko

# todo - потрібно добавити такі мови як - el, la, vi, th, ar, he та після потрібно видалити російську


import os
import json


def load_localization(language):
    localization_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(localization_folder, f'{language}.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return None


def translate_text(text, language):
    localization = load_localization(language)
    if text in localization[language]:
        return localization[language][text]
    else:
        localization_en = load_localization('en')
        if text in localization_en['en']:
            return localization_en['en'][text]
        return text


