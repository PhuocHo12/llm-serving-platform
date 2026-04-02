from api.routers import chat_router

from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(chat_router.router)