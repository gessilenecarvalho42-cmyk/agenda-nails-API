from pydantic import BaseModel, Field
from typing import Optional

class ManicureCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    phone: str = Field(min_length=8, max_length=20)
    address: Optional[str] = Field(default=None, max_length=150)

class ManicureUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    phone: Optional[str] = Field(default=None, min_length=8, max_length=20)
    address: Optional[str] = Field(default=None, max_length=150)

class ManicureResponse(ManicureCreate):
    id: int
    active: bool
    model_config = {"from_attributes": True}
