from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: str = "CLIENTE"
    client_id: Optional[int] = None


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: str
    client_id: Optional[int] = None

    class Config:
        from_attributes = True