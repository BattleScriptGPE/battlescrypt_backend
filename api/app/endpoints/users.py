from fastapi import APIRouter 
from fastapi import Query 
from typing import Optional 
from app.internal import database as db 
from fastapi.responses import JSONResponse 
import time 
import jwt 

JWT_SECRET = "secret" 
JWT_ALGO = "HS256" 
router = APIRouter( 
    prefix="/users", 
    tags=["User"], 
    responses={404: {"description" : "Not found"}}, 
) 
@router.get("/") 
async def default_user(): 
    return {"msg" : "c'est cool"}

@router.get("/list")
async def get_list():
    result = db.get_list_user()
    return result

@router.post("/register")
async def register_user(mail: str ,name: str ,username: str , password: str):
    result = db.push_user(name , username , password , mail)
    if result == 1:
        return {"message" : "création de l'utilisateur réussi"}
    else:
        return {"message" : "création de l'utilisateur non réussi"}

@router.post("/login")
async def login_user(username: str, password: str):
    result = db.get_user(username , password)
    encoded_jwt = jwt.encode({"username" : result[0][2] , "role" : result[0][5] , "id" : result[0][0] }, JWT_SECRET,algorithm=JWT_ALGO)
    return encoded_jwt

@router.put("/update")
async def update_user(token: str , mail: Optional[str] = None , name: Optional[str] = None , username: Optional[str] = None, password: Optional[str] = None):
    result = db.update_user(token , name , username , mail , password)
    return result

@router.delete("/del")
async def delete_user(token: str , id: int):
    result = db.delete_user(token , id)
    return result
