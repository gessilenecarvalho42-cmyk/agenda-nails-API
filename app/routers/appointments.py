from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.appointment import Appointment
from app.models.client import Client
from app.models.manicure import Manicure
from app.models.service import Service
from app.schemas.appointment import AppointmentCreate, AppointmentResponse


router = APIRouter(
    prefix="/api/appointments",
    tags=["Appointments"]
)


@router.post(
    "/",
    response_model=AppointmentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_appointment(
    appointment: AppointmentCreate,
    db: Session = Depends(get_db)
):
    client = db.query(Client).filter(
        Client.id == appointment.client_id
    ).first()

    if not client:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado."
        )

    manicure = db.query(Manicure).filter(
        Manicure.id == appointment.manicure_id
    ).first()

    if not manicure:
        raise HTTPException(
            status_code=404,
            detail="Manicure não encontrada."
        )

    service = db.query(Service).filter(
        Service.id == appointment.service_id
    ).first()

    if not service:
        raise HTTPException(
            status_code=404,
            detail="Serviço não encontrado."
        )

    new_appointment = Appointment(
        date=appointment.date,
        time=appointment.time,
        status=appointment.status,
        client_id=appointment.client_id,
        manicure_id=appointment.manicure_id,
        service_id=appointment.service_id
    )

    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    return new_appointment


@router.get(
    "/",
    response_model=list[AppointmentResponse]
)
def list_appointments(
    db: Session = Depends(get_db)
):
    return db.query(Appointment).all()


@router.get(
    "/{appointment_id}",
    response_model=AppointmentResponse
)
def get_appointment(
    appointment_id: int,
    db: Session = Depends(get_db)
):
    appointment = db.query(Appointment).filter(
        Appointment.id == appointment_id
    ).first()

    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Agendamento não encontrado."
        )

    return appointment