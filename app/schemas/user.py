from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    phone: str
    password: str
    role: str = "CLIENTE"
    client_id: Optional[int] = None


class UserResponse(BaseModel):
    id: int
    phone: str
    role: str
    client_id: Optional[int] = None

    model_config = {"from_attributes": True}


class LoginRequest(BaseModel):
    phone: str
    password: str