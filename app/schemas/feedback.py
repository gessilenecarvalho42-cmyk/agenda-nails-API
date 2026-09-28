from typing import Optional

from pydantic import BaseModel, Field


class FeedbackCreate(BaseModel):
    rating: int = Field(ge=1, le=5)
    comment: Optional[str] = None
    appointment_id: int


class FeedbackResponse(BaseModel):
    id: int
    rating: int
    comment: Optional[str] = None
    appointment_id: int

    model_config = {"from_attributes": True}