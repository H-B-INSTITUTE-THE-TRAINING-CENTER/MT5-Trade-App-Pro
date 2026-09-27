from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./hb_tradepro.db"

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