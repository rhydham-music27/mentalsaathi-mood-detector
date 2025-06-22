from fastapi import FastAPI
from app.routes import mood

app = FastAPI(title="Mood Detection API", version="1.0")

# Register mood detection route
app.include_router(mood.router)
