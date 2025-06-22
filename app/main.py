import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import mood

app = FastAPI(title="Mood Detection API", version="1.0")

app.include_router(mood.router)

# Optional: CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
