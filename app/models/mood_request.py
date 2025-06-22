from pydantic import BaseModel

class MoodRequest(BaseModel):
    text: str

class MoodResponse(BaseModel):
    mood: str
    confidence: float
