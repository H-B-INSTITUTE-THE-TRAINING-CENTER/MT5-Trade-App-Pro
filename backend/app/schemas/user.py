from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr, Field

class UserCreate(BaseModel):
    email:EmailStr
    full_name:str = Field(min_length=2, max_length=100)

    model_config = ConfigDict(extra="forbid")

class UserRead(BaseModel):
    id:int
    email:EmailStr
    full_name:str
    is_active:bool
    created_at:datetime

    model_config = ConfigDict(from_attributes=True)

class UserUpdate(BaseModel):
    email:EmailStr
    full_name: str = Field(
        min_length=2,
        max_length=100
    )

    model_config = ConfigDict(extra="forbid")