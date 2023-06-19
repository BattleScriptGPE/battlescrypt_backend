from fastapi import APIRouter

router = APIRouter(
    prefix="/stats",
    tags=["Stats"],
    responses={404: {"description": "Not found"}},
)


@router.get("/testing")
async def testing_stats():
    json_return = {
        "message" : "This is test message"
    }
    return json_return
