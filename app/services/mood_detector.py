from transformers import pipeline

# Load model once on startup
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

def detect_mood(text: str) -> dict:
    result = classifier(text)[0]
    top_result = max(result, key=lambda x: x['score'])
    return {
        "mood": top_result["label"],
        "confidence": round(top_result["score"], 2)
    }
