from fastapi import APIRouter, HTTPException
import httpx
from app.core.config import settings

router = APIRouter(prefix="/users", tags=["User Service"])

@router.get("/")
async def get_users():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{settings.USER_SERVICE_URL}/users")
            response.raise_for_status()  # Raises exception for 4xx/5xx
            return response.json()
    except httpx.ConnectError:
        raise HTTPException(status_code=502, detail="User service unavailable at the moment.")
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gateway internal error: {str(e)}")
