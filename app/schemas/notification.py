from pydantic import BaseModel, Field


class NotificationCreate(BaseModel):
    message: str = Field(min_length=1, max_length=255)
    appointment_id: int


class NotificationResponse(BaseModel):
    id: int
    message: str
    read: bool
    appointment_id: int

    model_config = {"from_attributes": True}
