from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserRead, UserUpdate

def create_user(user_data: UserCreate, db: Session) -> User:
    user = User(
        email = str(user_data.email),
        full_name = user_data.full_name
    )

    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise ValueError("A user with this email may already exists")

    return user
    