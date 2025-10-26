from fastapi import APIRouter, Request
import httpx
from app.core.config import settings

router = APIRouter(prefix="/users", tags=["User Service"])

@router.get("/")
async def get_users():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{settings.USER_SERVICE_URL}/users")
        return response.json()
