from pydantic import BaseModel


class userLoginDto(BaseModel):
    mail: str
    password: str
    
class userRegisterDto(BaseModel):
    firstname: str
    lastname: str
    age: int
    mail: str
    username: str
    password: str
    