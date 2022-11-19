from fastapi import APIRouter
from fastapi import Query
from typing import Optional


router = APIRouter(
    prefix="/stats",
    tags=["Stats"],
    responses={404: {"description" : "Not found"}},
)

@router.get("/")
async def default_stats():
    return {"msg" : "c'est cool"}