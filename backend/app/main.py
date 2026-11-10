
from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.analyze import router as analyze_router

app = FastAPI(title="Callus Authorship Detector API")

# Allow requests from the deployed frontend and local development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ai-admissions-essay-detector.vercel.app",
        "http://localhost:5173",
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


@app.get("/", tags=["health"])
def root():
    return {
        "status": "ok",
        "service": "Callus Authorship Detector API",
        "docs": "/docs",
    }


@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}


app.include_router(analyze_router, prefix="/api")
