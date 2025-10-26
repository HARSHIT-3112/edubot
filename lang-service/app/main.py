from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Language Service (Level0)")

@app.get("/health")
async def health():
    return {"service": "lang", "status": "ok"}

class TextReq(BaseModel):
    text: str

@app.post("/detect")
async def detect(req: TextReq):
    # not doing actual detection on day 1; return placeholder
    return {"language": "en"}
