from sqlalchemy import text

from app.db.database import engine

with engine.connect() as connection:
    result = connection.execute(
        text("SELECT current_database(), current_user")
    )

    database_name, username = result.fetchone()

    print("Database:",database_name)
    print("User:",username)
    print("Postgre connection successfull")