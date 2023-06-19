from fastapi import APIRouter
from app.endpoints import achievement_controller , auth_controller , stats_controller , user_controller

router = APIRouter()
router.include_router(achievement_controller.router)
router.include_router(auth_controller.router)
router.include_router(stats_controller.router)
router.include_router(user_controller.router)