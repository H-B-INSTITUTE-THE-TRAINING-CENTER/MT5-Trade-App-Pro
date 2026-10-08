from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.base import Base

DATABASE_URL = "sqlite:///./Mt5TradeAppPro.db"

engine = create_engine(
    DATABASE_URL,
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