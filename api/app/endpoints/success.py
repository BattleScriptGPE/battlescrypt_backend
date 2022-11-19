from fastapi import APIRouter
from fastapi import Query
from typing import Optional


router = APIRouter(
    prefix="/success",
    tags=["Success"],
    responses={404: {"description" : "Not found"}},
)

@router.get("/")
async def default_success():
    return {"msg" : "c'est cool"}