from pydantic import BaseModel

from enum import Enum, unique


class UserModel:
    def __init__(self, id, age, gender, like_gender, location, games, description, photo):
        self.id: int = id
        self.age: int = age
        self.gender: str = gender
        self.like_gender: str = like_gender
        self.location: str = location
        self.games: str = games
        self.description: str = description
        self.photo: str = photo
