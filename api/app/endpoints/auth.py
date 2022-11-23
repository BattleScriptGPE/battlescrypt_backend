from fastapi import APIRouter 
from fastapi import Query 
from fastapi.responses import JSONResponse
import app.models.User as modelsUser
import app.internal.database as database
import logging
import app.internal.password as pwd
import app.internal.token as token

router = APIRouter( 
    tags=["Auth"],
    responses={404: {"description" : "Not found"}}, 
)


@router.get("/") 
async def default_user(): 
    return {"msg" : "default route for api"}

@router.post("/register")
async def register_user(name: str , username: str , password: str , mail: str):
    db = database.get_db()
    userSearch = db.query(modelsUser.User).filter(modelsUser.User.mail == mail).first()
    if userSearch is None:
        password = pwd.encrypt_password(password)
        db_user = modelsUser.User(name=name , username=username , password=password, mail=mail, role=0)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        logging.info(" [SQL] : Push to DB Ok")
        return db_user
    else:
        return {"error" : "this mail already exist"}

@router.get("/login")
async def login_user(mail: str , password: str):
    db = database.get_db()
    password = pwd.encrypt_password(password)
    userSearch = db.query(modelsUser.User).filter(modelsUser.User.mail == mail , modelsUser.User.password == password).first()
    if userSearch is None:
        return {"error" : "verify mail/password"}
    else:
        token_jwt = token.create_token(userSearch.id , userSearch.name , userSearch.role)
        return {"token" : token_jwt}


