from pydantic import BaseModel

from enum import Enum, unique


class UserModel(BaseModel):
    user_id: int
    user_name: str
    user_age: int
    user_gender: str
    user_like_gender: str
    user_location: str
    user_games: str
    user_description: str
    user_photo: str
    user_language: str
    user_likes: int = 0
