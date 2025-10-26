from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import user_routes
from app.middleware.logging_middleware import LoggingMiddleware
from app.middleware.auth_middleware import AuthMiddleware
from app.routes import user_routes, forward_routes, health_routes
from app.middleware.error_handler import ErrorHandlerMiddleware



app = FastAPI(title="Gateway Service (Level0)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


# Add error handling middleware
app.add_middleware(ErrorHandlerMiddleware)
# Add custom logging middleware
app.add_middleware(LoggingMiddleware)
# Add authentication middleware
app.add_middleware(AuthMiddleware)




# Include routers
app.include_router(user_routes.router)
app.include_router(health_routes.router)
app.include_router(forward_routes.router)

@app.get("/")
def root():
    return {"message": "Gateway Service is running 🚀"}

from app.services.health_service import get_all_service_status

@app.get("/health")
async def health():
    return await get_all_service_status()


@app.on_event("startup")
async def list_routes():
    print("\n🔍 Registered Routes:")
    for route in app.routes:
        print(" ", route.path)
    print("✅ Ready!\n")
