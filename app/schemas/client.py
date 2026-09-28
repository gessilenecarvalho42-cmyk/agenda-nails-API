from pydantic import BaseModel, Field
from typing import Optional

class ClientCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    phone: str = Field(min_length=8, max_length=20)
    consent_whatsapp: bool = False

class ClientUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    phone: Optional[str] = Field(default=None, min_length=8, max_length=20)
    consent_whatsapp: Optional[bool] = None

class ClientResponse(ClientCreate):
    id: int
    active: bool
    model_config = {"from_attributes": True}
