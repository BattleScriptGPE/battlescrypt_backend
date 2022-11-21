from fastapi import APIRouter 
from fastapi import Query 
from fastapi.responses import JSONResponse
import app.models.User as modelsUser
from app.internal.database import SessionLocal , engine

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
    db = SessionLocal()
    db_user = modelsUser.User(name="test" , username="test" , password="test", mail="test",role=1)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
