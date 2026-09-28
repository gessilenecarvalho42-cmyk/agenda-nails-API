from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


class ServiceCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=200)
    price: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    duration: str = Field(min_length=1, max_length=50)


class ServiceUpdate(BaseModel):
    name: Optional[str] = Field(
        default=None,
        min_length=1,
        max_length=100
    )
    description: Optional[str] = Field(
        default=None,
        min_length=1,
        max_length=200
    )
    price: Optional[Decimal] = Field(
        default=None,
        gt=0,
        max_digits=10,
        decimal_places=2
    )
    duration: Optional[str] = Field(
        default=None,
        min_length=1,
        max_length=50
    )


class ServiceResponse(BaseModel):
    id: int
    name: str
    description: str
    price: Decimal
    duration: str

    model_config = {"from_attributes": True}