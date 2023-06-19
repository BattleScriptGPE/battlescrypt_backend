from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)


@router.get("/testing")
async def testing_authentication():
    json_return = {
        "message": "This is test message"
    }
    return json_return
