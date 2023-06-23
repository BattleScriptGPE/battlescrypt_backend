import json
import logging
from datetime import datetime , timedelta
from typing import Optional
import jwt
import app.utils.database_utils as database
from fastapi import APIRouter , Depends, HTTPException, status , Request
from app.models.models_all import User , Achievement , UserAchievements
from app.dtos.userDto import userLoginDto , userRegisterDto
from app.dtos.achievementDto import achievementPostDto
from app.utils.token_utils import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    ALGORITHM,
    JWT_SECRET_KEY,
    verify_token,
)

router = APIRouter(
    prefix="/achievement",
    tags=["Achievement"],
    responses={404: {"description": "Not found"}},
)

db = database.get_db()

@router.get("/testing")
async def testing_achievement():
    json_return = {
        "message" : "This is test message"
    }
    return json_return

@router.get("/all")
async def get_all_achievement(authorized: bool = Depends(verify_token)):
    result = db.query(Achievement).all()
    if result is None:
        raise HTTPException(status_code=404)
    return result

@router.post("/create")
async def post_achievement(achievementPostDto: achievementPostDto ,req: Request , authorized: bool = Depends(verify_token)):
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
    result: Achievement = Achievement(
        xp_value=achievementPostDto.xp,
        name=achievementPostDto.name,
        description=achievementPostDto.description,
        metas=achievementPostDto.metas,
    )
    db.add(result)
    db.commit()
    return achievementPostDto

@router.get("/me")
async def get_achievement_user(req: Request, authorized: bool = Depends(verify_token)):
    token = req.headers["Authorization"]
    token_parsed = str.replace(str(token) , "Bearer ", "")
    token_decoded = jwt.decode(token_parsed , JWT_SECRET_KEY, ALGORITHM)
    token_dump = json.dumps(token_decoded)
    token_dump = json.loads(token_dump)
    result = db.query(User).filter(User.mail == token_dump["sub"]).first()
    if result is None:
        raise HTTPException(status_code=404)
    result_achievement = db.query(UserAchievements).filter(UserAchievements.id_user == result.id).all()
    return result_achievement

@router.post("/user/{achievement_id}")
async def set_achievement_to_user(achievement_id: int , req: Request , authorized: bool = Depends(verify_token)):
    token = req.headers["Authorization"]
    token_parsed = str.replace(str(token) , "Bearer " , "")
    token_decoded = jwt.decode(token_parsed , JWT_SECRET_KEY, ALGORITHM)
    token_dump = json.dumps(token_decoded)
    token_dump = json.loads(token_dump)
    result = db.query(User).filter(User.mail == token_dump["sub"]).first()
    if result is None:
        raise HTTPException(status_code=404)
    result_achi = db.query(User).filter(UserAchievements.id_user == result.id , UserAchievements.id_achievement == achievement_id).first()
    if result_achi is not None:
        raise HTTPException(status_code=404)
    result_achievement: UserAchievements = UserAchievements(
        id_achievement=achievement_id,
        id_user=result.id,
        done_at=datetime.now(),
    )
    db.add(result_achievement)
    db.commit()
    result_achievement = db.query(UserAchievements).filter(UserAchievements.id_achievement == achievement_id).first()
    return result_achievement

