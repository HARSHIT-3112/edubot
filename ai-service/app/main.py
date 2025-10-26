from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Service (Level0)")

@app.get("/health")
async def health():
    return {"service": "ai", "status": "ok"}

class GenerateRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate(req: GenerateRequest):
    # stub: simple echo reply for level 0
    return {"reply": f"[stub AI reply] received prompt: {req.prompt[:200]}"}
