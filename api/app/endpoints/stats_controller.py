from fastapi import APIRouter
import app.utils.database_utils as database
from fastapi import APIRouter , Depends, HTTPException, status
from app.models.models_all import Download
router = APIRouter(
    prefix="/stats",
    tags=["Stats"],
    responses={404: {"description": "Not found"}},
)

db = database.get_db()

@router.get("/testing")
async def testing_stats():
    json_return = {
        "message" : "This is test message"
    }
    return json_return


@router.post("/push")
async def push_download():
    result: Download = Download(
        nb_download=1
    )
    db.add(result)
    db.commit()
    raise HTTPException(status_code=200)