from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="Stock Market & MT5 Trading Platform",
    version=settings.app_version
)


@app.get("/")
def home():
    return {
        "message": f"Welcome {settings.app_name}"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "environment":settings.environment
    }

@app.get("/about")
def about():
    return {
        "application": settings.app_name,
        "developer": "Shyam Bhojak",
        "technology": "Python + FastAPI"
    }

@app.get("/version")
def version():
    return{
        "version":settings.app_version,
        "status":settings.environment   
    }