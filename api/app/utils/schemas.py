from typing import List, Optional
from pydantic import BaseModel
from typing import Union

class UserConnect(BaseModel):
    username: str
    password: str

class UserBase(BaseModel):
    firstname: str
    lastname: str
    age: int
    mail: str
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_admin: bool

    class Config:
        orm_mode = True

class UserStats(User):
    time_played: str
    wins: int
    defeats: int
    line_coded: int
    last_connexion: str
    experience: int
    created_at: str

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
