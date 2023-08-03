import os
import sys

import unittest
from utils.funcs import check_location


def test_pass():
    result = check_location("12345")
    assert result is None


def test_check_location():
    print("Тестуємо рядок, який складається тільки з цифр")
    result = check_location("12345")
    assert result is None

    print("Тестуємо рядок, який містить як цифри, так і літери")
    result = check_location("New York123")
    assert result is None

    print("Тестуємо рядок, який представляє коректне місцезнаходження")
    result = check_location("New York")
    assert result is not None

    print("Тестуємо рядок, який представляє некоректне місцезнаходження і викликає помилку Invalid Location")
    result = check_location("Invalid Location")
    assert result is None


if __name__ == '__main__':
    unittest.main()

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH,"src"
)
sys.path.append(SOURCE_PATH)
