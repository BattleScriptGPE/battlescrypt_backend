import json
from datetime import datetime , timedelta
from typing import Optional
import jwt
import app.utils.database_utils as database
from fastapi import APIRouter , Depends, HTTPException, status , Request
from app.models.models_all import User
from app.dtos.userDto import userLoginDto , userRegisterDto
from app.utils.token_utils import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    ALGORITHM,
    JWT_SECRET_KEY,
    verify_token,
)


router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)

db = database.get_db()

@router.get("/testing")
async def testing_user():
    json_return = {
        "message" : "This is test message"
    }
    return json_return

@router.get("/me")
async def get_me(req: Request , authorized: bool = Depends(verify_token)):
    token = req.headers["Authorization"]
    token_parsed = str.replace(str(token), "Bearer ", "")
    token_decoded = jwt.decode(token_parsed , JWT_SECRET_KEY, ALGORITHM)
    token_dump = json.dumps(token_decoded)
    token_dump = json.loads(token_dump)
    result = db.query(User).filter(User.mail == token_dump["sub"]).first()
    if result is None:
        raise HTTPException(status_code=404)
    json_return = {
        "id": result.id,
        "mail": result.mail,
        "password": result.password,
        "username": result.username,
        "firstname": result.firstname,
        "lastname": result.lastname,
        "created_at": result.created_at.isoformat(),
        "updated_at": result.updated_at.isoformat(),
    }
    return json_return

@router.get("/{user_id}", status_code=200)
async def get_user(user_id: int , req: Request ,  authorized: bool = Depends(verify_token)):
    token = req.headers["Authorization"]
    token_parsed = str.replace(str(token) , "Bearer " , "")
    token_decoded = jwt.decode(token_parsed , JWT_SECRET_KEY, ALGORITHM)
    token_dump = json.dumps(token_decoded)
    token_dump = json.loads(token_dump)
    result = db.query(User).filter(User.mail == token_dump["sub"]).first()
    if result is None:
        raise HTTPException(status_code=404)
    if result.is_admin == False:
        raise HTTPException(status_code=401)
    result = db.query(User).filter(User.id == user_id).first()
    json_return = {
        "id": result.id,
        "mail": result.mail,
        "password": result.password,
        "username": result.username,
        "firstname": result.firstname,
        "lastname": result.lastname,
        "created_at": result.created_at.isoformat(),
        "updated_at": result.updated_at.isoformat(),
    }
    return json_return
