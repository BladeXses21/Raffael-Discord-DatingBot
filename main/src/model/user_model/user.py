import array

from pydantic import BaseModel, Field


class UserForm(BaseModel):
    user_id: int = Field(..., title='User ID')
    name: str = Field(..., title='Name')
    age: int = Field(..., title='Age')
    gender: str = Field(..., title='Gender')
    opposite_gender: str = Field(..., title='Opposite Gender')
    location: list = Field(..., title='Location')
    games: str = Field(..., title='Games')
    description: str = Field(..., title='Description')
    photo: str = Field(..., title='Photo')
    language: str = Field(..., title='Language')
    likes: int = Field(0, title='Likes')


class UserConfirmation(BaseModel):
    user_id: int = Field(..., title='User ID')
    confirmed: bool = Field(False, title='Confirmed')
