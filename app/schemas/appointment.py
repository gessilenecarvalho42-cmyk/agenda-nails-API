from datetime import date, time
from pydantic import BaseModel


class AppointmentCreate(BaseModel):
    date: date
    time: time
    status: str = "CONFIRMADO"
    client_id: int
    manicure_id: int
    service_id: int


class AppointmentResponse(BaseModel):
    id: int
    date: date
    time: time
    status: str
    client_id: int
    manicure_id: int
    service_id: int

    model_config = {"from_attributes": True}
