from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.base import Base
from app.core.config import settings


engine = create_engine(
    settings.database_url,
    echo=True
)

# with engine.connect() as connection:
#     print("Database Connection Successful!")


SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,   
    autoflush=False
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    Base.metadata.create_all(bind=engine)