import httpx
from fastapi import Request
from app.core.config import settings
import asyncio

# Helper for retries
async def send_with_retry(method, url, headers, body, retries=2, timeout=5.0):
    for attempt in range(retries + 1):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.request(
                    method=method,
                    url=url,
                    headers=headers,
                    content=body,
                    timeout=timeout
                )
                return response
        except httpx.RequestError as e:
            if attempt < retries:
                await asyncio.sleep(1)  # short delay
                continue
            raise e  # bubble up after retries

async def forward_request(request: Request):
    path = request.url.path
    print(f"🧭 Forwarding request: {path}")

    if path.startswith("/users"):
        print("→ Routing to USER_SERVICE")
        target_url = settings.USER_SERVICE_URL + path
    elif path.startswith("/documents"):
        print("→ Routing to DOCUMENT_SERVICE")
        target_url = settings.DOCUMENT_SERVICE_URL + path
    elif path.startswith("/ai"):
        print("→ Routing to AI_SERVICE")
        target_url = settings.AI_SERVICE_URL + path
    elif path.startswith("/lang"):
        print("→ Routing to LANG_SERVICE")
        target_url = settings.LANG_SERVICE_URL + path
    else:
        print("⚠️ Unknown route prefix:", path)
        return {"error": "Unknown route prefix"}, 404


    if request.url.query:
        target_url += f"?{request.url.query}"

    headers = dict(request.headers)
    headers.pop("host", None)
    body = await request.body()

    try:
        response = await send_with_retry(
            method=request.method,
            url=target_url,
            headers=headers,
            body=body,
        )

        try:
            return response.json(), response.status_code
        except ValueError:
            return {"text": response.text}, response.status_code

    except httpx.RequestError as e:
        return {
            "success": False,
            "message": "Service unreachable after retries",
            "error": str(e)
        }, 503

