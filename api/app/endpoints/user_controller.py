from datetime import datetime , timedelta
from typing import Optional
import jwt
import app.utils.database_utils as database
from fastapi import APIRouter , Depends, HTTPException, status
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

@router.get("/{user_id}", status_code=200)
async def get_user(user_id: int , authorized: bool = Depends(verify_token)):
    result = db.query(User).filter(User.id == user_id).first()
    if result is None:
        raise HTTPException(status_code=404)
    json_return = {
        "id": result.id,
        "mail": result.mail,
        "password": result.password,
        "created_at": result.created_at.isoformat(),
        "updated_at": result.updated_at.isoformat(),
    }
    return json_return