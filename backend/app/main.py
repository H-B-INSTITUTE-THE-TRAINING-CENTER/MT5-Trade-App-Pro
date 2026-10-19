from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import text,select
from sqlalchemy.exc import IntegrityError



from app.core.config import settings
from app.db.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserRead

from app.api.routes.users import router as users_router


app = FastAPI(
    title=settings.app_name,
    description="Stock Market & MT5 Trading Platform",
    version=settings.app_version
)

app.include_router(users_router)


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




@app.get("/users",response_model=list[UserRead])
def get_users(db:Session = Depends(get_db)):
    
    statement = select(User).order_by(User.id)
    users = db.scalars(statement).all()
    return users

@app.get("/users/{user_id}",response_model=UserRead)
def get_user(user_id:int, db:Session = Depends(get_db)):
    
    user = db.get(User,user_id)
    if user is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "User not found"
        )

    return user

