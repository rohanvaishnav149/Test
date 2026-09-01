from pydantic import BaseModel, EmailStr
from datetime import datetime


# Base schema
class UserBase(BaseModel):
    name: str
    email: EmailStr
    age: int


# Schema for creating a user
class UserCreate(UserBase):
    pass


# Schema for updating a user
class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    age: int | None = None


# Schema for returning user data
class UserResponse(UserBase):
    id: int
    # is_active: bool
    # created_at: datetime

    model_config = {
        "from_attributes": True  # Required for SQLAlchemy ORM models (Pydantic v2)
    }