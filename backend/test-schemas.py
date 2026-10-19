from pydantic import ValidationError
from app.schemas.user import UserCreate
try:

    user = UserCreate(
        email="not-an-email",
        full_name="A"
    )
except ValidationError as error:
    print(error)
