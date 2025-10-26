import httpx
from app.core.config import settings

# Utility function to check each service's health endpoint
async def check_service_health(name: str, url: str):
    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            response = await client.get(f"{url}/health")
            if response.status_code == 200:
                return {name: "healthy"}
            else:
                return {name: f"unhealthy ({response.status_code})"}
    except Exception as e:
        return {name: f"down ({str(e)})"}


async def get_all_service_status():
    # Each service + their URLs from env
    services = {
        "gateway": "healthy",  # self status
        "user-service": settings.USER_SERVICE_URL,
        "document-service": settings.DOCUMENT_SERVICE_URL,
        "ai-service": settings.AI_SERVICE_URL,
        "lang-service": settings.LANG_SERVICE_URL,
    }

    status_report = {}

    for name, url in services.items():
        if name == "gateway":
            status_report[name] = "healthy"
        else:
            health = await check_service_health(name, url)
            status_report.update(health)

    return status_report
