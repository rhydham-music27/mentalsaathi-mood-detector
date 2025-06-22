from transformers import pipeline

# Load model once on startup
classifier = pipeline("sentiment-analysis")  # default is `distilbert`, much smaller

def detect_mood(text: str) -> dict:
    result = classifier(text)[0]
    top_result = max(result, key=lambda x: x['score'])
    return {
        "mood": top_result["label"],
        "confidence": round(top_result["score"], 2)
    }
