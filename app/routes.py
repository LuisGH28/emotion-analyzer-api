from fastapi import APIRouter, UploadFile, File
from app.services.emotion_service import analyze_emotion_from_bytes

router = APIRouter(prefix="", tags=["emotion"])

@router.post("/analyze_emotion")
async def analyze_emotion(file: UploadFile = File(...)):
    data = await file.read()
    return analyze_emotion_from_bytes(data)
