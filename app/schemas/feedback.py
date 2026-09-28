from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class FeedbackCreate(BaseModel):
    comment: str = Field(min_length=1, max_length=300)
    appointment_id: int

class FeedbackResponse(FeedbackCreate):
    id: int
    sent_date: date
    model_config = {"from_attributes": True}
