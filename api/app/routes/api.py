from fastapi import APIRouter
from app.endpoints import users,success,stats

router = APIRouter()
router.include_router(users.router)
router.include_router(success.router)
router.include_router(stats.router)