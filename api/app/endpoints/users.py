from fastapi import APIRouter 
from fastapi import Query 
from fastapi.responses import JSONResponse 

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
