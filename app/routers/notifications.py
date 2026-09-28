from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.notification import Notification
from app.models.appointment import Appointment
from app.schemas.notification import NotificationCreate, NotificationResponse


router = APIRouter(
    prefix="/api/notifications",
    tags=["Notifications"]
)


@router.post(
    "/",
    response_model=NotificationResponse,
    status_code=status.HTTP_201_CREATED
)
def create_notification(
    notification: NotificationCreate,
    db: Session = Depends(get_db)
):
    appointment = db.query(Appointment).filter(
        Appointment.id == notification.appointment_id
    ).first()

    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Agendamento não encontrado."
        )

    new_notification = Notification(
        message=notification.message,
        appointment_id=notification.appointment_id,
        read=False
    )

    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)

    return new_notification


@router.get(
    "/",
    response_model=list[NotificationResponse]
)
def list_notifications(
    db: Session = Depends(get_db)
):
    return db.query(Notification).all()


@router.get(
    "/{notification_id}",
    response_model=NotificationResponse
)
def get_notification(
    notification_id: int,
    db: Session = Depends(get_db)
):
    notification = db.query(Notification).filter(
        Notification.id == notification_id
    ).first()

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notificação não encontrada."
        )

    return notification