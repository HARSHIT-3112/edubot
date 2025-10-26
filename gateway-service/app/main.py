from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import user_routes

app = FastAPI(title="Gateway Service (Level0)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(user_routes.router)

@app.get("/")
def root():
    return {"message": "Gateway Service is running 🚀"}

@app.get("/health")
async def health():
    return {"service": "gateway", "status": "ok"}
