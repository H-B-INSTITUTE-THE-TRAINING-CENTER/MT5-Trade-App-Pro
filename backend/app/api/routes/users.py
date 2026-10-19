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


@router.get("",response_model=list[UserRead])
def read_users(db:Session = Depends(get_db)):
    return user_service.get_users(db)

@router.get("/{user_id}", response_model=UserRead)
def read_user(user_id:int, db:Session = Depends(get_db)):
    user = user_service.get_user(user_id, db)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return user

@router.put("/{user_id}",response_model=UserRead)
def edit_user(user_id:int, user_data:UserUpdate, db:Session = Depends(get_db)):
    user = user_service.get_user(user_id, db)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")

    try:
        return user_service.update_user(user, user_data, db)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error)
        ) from error

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_user(user_id:int, db:Session = Depends(get_db)):
    user = user_service.get_user(user_id,db)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    
    user_service.delete_user(user,db)

    return None