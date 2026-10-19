from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

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


def get_users(db:Session) -> list[User]:
    statement = select(User).order_by(User.id)
    return list(db.scalars(statement).all())

def get_user(user_id:int, db:Session) -> User | None:
    return db.get(User,user_id)

def update_user(user:User,user_data:UserUpdate, db:Session) -> User:
    user.email = str(user_data.email)
    user.full_name = user_data.full_name

    try:
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise ValueError("A user with this email may already exists.")

    return user

def delete_user(user:User, db:Session) -> None:
    db.delete(user)
    db.commit()    
