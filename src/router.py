from auth.routes import router as auth
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(auth)
