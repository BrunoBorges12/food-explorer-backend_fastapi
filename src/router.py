from auth.routes import router as auth
from fastapi import APIRouter
from products.router import router as products

api_router = APIRouter()

api_router.include_router(auth)
api_router.include_router(products)
