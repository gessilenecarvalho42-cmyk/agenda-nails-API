from datetime import datetime

from pydantic import BaseModel, Field


class NotificationCreate(BaseModel):
    type: str = Field(min_length=1, max_length=50)
    message: str = Field(min_length=1, max_length=255)
    appointment_id: int


class NotificationResponse(BaseModel):
    id: int
    type: str
    message: str
    sent_date: datetime
    read: bool
    appointment_id: int

    model_config = {"from_attributes": True}
