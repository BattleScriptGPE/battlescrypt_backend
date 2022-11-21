from fastapi import APIRouter 
from fastapi import Query 
from fastapi.responses import JSONResponse
import app.models.User as modelsUser
import app.internal.database as database
import logging


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

@router.get("/test")
async def test():
    db = database.get_db()
    db_user = modelsUser.User(name="test" , username="test" , password="test", mail="test",role=1)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    logging.info("Push to DB Success")
    return db_user
