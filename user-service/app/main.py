from fastapi import FastAPI

app = FastAPI(title="User Service (Level0)")

@app.get("/health")
async def health():
    return {"service": "user", "status": "ok"}
