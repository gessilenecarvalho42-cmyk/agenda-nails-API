from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class AppointmentCreate(BaseModel):
    date: date
    time: time
    client_id: int
    manicure_id: int
    service_id: int

class AppointmentResponse(AppointmentCreate):
    id: int
    status: str
    model_config = {"from_attributes": True}

class AppointmentStatusUpdate(BaseModel):
    status: str
