from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import UserCreate, UserUpdate, UserRead
from app.services import user_service

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("",response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate, db:Session = Depends(get_db)):
    try:
        return user_service.create_user(user_data,db)
    except ValueError as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(error)) from error