from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text


from app.core.config import settings
from app.db.database import get_db


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

@app.get("/database-test")
def database_test(db:Session = Depends(get_db)):
    result = db.execute(text("SELECT 1"))
    value = result.scalar()

    return {
        "database":"connected",
        "test_result":value
    }

@app.get("/database-info")
def database_info(db:Session = Depends(get_db)):
    return{
        "database": "SQLite",
        "orm": "SQLAlchemy",
        "status": "connected"
    }