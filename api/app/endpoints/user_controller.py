from fastapi import APIRouter

router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)


@router.get("/testing")
async def testing_user():
    json_return = {
        "message" : "This is test message"
    }
    return json_return
