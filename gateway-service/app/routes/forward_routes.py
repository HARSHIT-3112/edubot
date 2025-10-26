from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.services.forward_service import forward_request

router = APIRouter()

@router.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def catch_all(request: Request, full_path: str):
    data, status = await forward_request(request)
    return JSONResponse(content=data, status_code=status)
