from fastapi import APIRouter
from app.services.health_service import get_all_service_status

router = APIRouter(prefix="/gateway", tags=["Gateway Health"])

@router.get("/status")
async def gateway_status():
    return await get_all_service_status()
