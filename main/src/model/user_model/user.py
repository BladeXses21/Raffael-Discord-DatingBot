from pydantic import BaseModel, Field


class UserForm(BaseModel):
    user_id: int = Field(..., title='User ID', description='This field defines the id of the user who created the questionnaire')
    name: str = Field(..., title='Name', description='This field defines the name of the user who created the questionnaire')
    age: int = Field(..., title='Age', description='This field determines the age of the user who created the questionnaire')
    gender: str = Field(..., title='Gender', description='This field determines the gender of the user who created the questionnaire')
    opposite_gender: str = Field(..., title='Opposite Gender',
                                 description='This field defines the gender of the user by which the questionnaire will be searched')
    location: list = Field(..., title='Location',
                           description='This field defines the location by which the search will be carried out in the future ')
    games: str = Field(..., title='Games',
                       description='This field defines the games that the user specifies when creating or editing a questionnaire')
    description: str = Field(..., title='Description',
                             description='This field defines the description of the questionnaire by the user who creates it')
    photo: str = Field(..., title='Photo', description='This field defines the photo or picture provided by the user during registration')
    language: str = Field(..., title='Language', description='This field defines the language of the user interface of the discord')
    likes: int = Field(0, title='Likes', description='This field indicates the number of preferences that the user has left for user profiles.')


class UserConfirmation(BaseModel):
    user_id: int = Field(..., title='User ID', description='This field defines the id of the user who created the questionnaire')
    confirmed: bool = Field(False, title='Confirmed', description='This field determines whether the user has confirmed the rules for using the bot')


