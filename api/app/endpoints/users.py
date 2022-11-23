from fastapi import APIRouter 
from fastapi import Query
from typing import Optional 
from fastapi.responses import JSONResponse
import app.models.User as modelsUser
import app.internal.database as database
import logging
import app.internal.password as pwd
import app.internal.token as token

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description" : "Not found"}}, 
)

@router.get("/list")
async def get_user_list():
    db = database.get_db()
    userList = db.query(modelsUser.User).all()
    for raw in userList:
        raw.password = "hidden"
    return userList

@router.get("/current")
async def get_current_user(jwt: str):
    decoded_token = token.decode_token(jwt)
    db = database.get_db()
    return db.query(modelsUser.User).filter(modelsUser.User.id == decoded_token["id"]).first()

@router.put("/update")
async def update_current_user(jwt: str , name: Optional[str] = None , username: Optional[str] = None , mail: Optional[str] = None , password: Optional[str] = None ):
    decoded_token = token.decode_token(jwt)
    db = database.get_db()
    userToChange = db.query(modelsUser.User).filter(modelsUser.User.id == decoded_token["id"]).first()
    if name is not None:
        userToChange.name = name
    if username is not None:
        userToChange.username = username
    if mail is not None:
        userToChange.mail = mail
    if password is not None:
        password = pwd.encrypt_password(password)
        userToChange.password = password
    db.add(userToChange)
    db.commit()
    db.refresh(userToChange)
    return userToChange
