from fastapi import APIRouter

router = APIRouter(
    prefix="/achievement",
    tags=["Achievement"],
    responses={404: {"description": "Not found"}},
)


@router.get("/testing")
async def testing_achievement():
    json_return = {
        "message" : "This is test message"
    }
    return json_return
