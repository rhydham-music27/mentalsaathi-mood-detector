from fastapi import APIRouter, Depends, HTTPException, status
from app.models.mood_request import MoodRequest, MoodResponse
from app.services.mood_detector import detect_mood
from app.auth.jwt_handler import verify_token

router = APIRouter()

@router.post("/detect-mood", response_model=MoodResponse)
def get_mood(data: MoodRequest, token: str = Depends(verify_token)):
    try:
        return detect_mood(data.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.get("/ping")
def ping():
    return {"message": "Mood Detection API is alive 🚀"}