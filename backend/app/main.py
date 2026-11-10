from __future__ import annotations

from fastapi import FastAPI
from backend.app.api.analyze import router as analyze_router

app = FastAPI(title="Callus Authorship Detector API")


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