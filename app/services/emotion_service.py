import cv2
import numpy as np
from emotion.detector import analyze_emotion_from_frame  # ← tu paquete 'emotion'
from app.config import settings

def analyze_emotion_from_bytes(image_bytes: bytes) -> dict:
    arr = np.frombuffer(image_bytes, np.uint8)
    bgr = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    if bgr is None:
        return {"ok": False, "error": "Imagen inválida (no se pudo decodificar)"}

    res = analyze_emotion_from_frame(
        bgr,
        detector_backend=settings.DETECTOR_BACKEND,
        enforce_detection=False,
    )
    emo_en = res.get("emotion_en")
    emo_es = res.get("emotion_es")
    score = float(res.get("score", 0.0))

    return {"ok": True, "emotion_en": emo_en, "emotion_es": emo_es, "score": score}
