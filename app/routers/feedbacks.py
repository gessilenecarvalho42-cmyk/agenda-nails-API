from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.appointment import Appointment
from app.models.feedback import Feedback
from app.schemas.feedback import FeedbackCreate, FeedbackResponse


router = APIRouter(
    prefix="/api/feedbacks",
    tags=["Feedbacks"]
)


@router.post(
    "/",
    response_model=FeedbackResponse,
    status_code=status.HTTP_201_CREATED
)
def create_feedback(
    feedback: FeedbackCreate,
    db: Session = Depends(get_db)
):
    appointment = db.query(Appointment).filter(
        Appointment.id == feedback.appointment_id
    ).first()

    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Agendamento não encontrado."
        )

    existing_feedback = db.query(Feedback).filter(
        Feedback.appointment_id == feedback.appointment_id
    ).first()

    if existing_feedback:
        raise HTTPException(
            status_code=400,
            detail="Este agendamento já possui uma avaliação."
        )

    new_feedback = Feedback(
        rating=feedback.rating,
        comment=feedback.comment,
        appointment_id=feedback.appointment_id
    )

    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)

    return new_feedback


@router.get(
    "/",
    response_model=list[FeedbackResponse]
)
def list_feedbacks(
    db: Session = Depends(get_db)
):
    return db.query(Feedback).all()


@router.get(
    "/{feedback_id}",
    response_model=FeedbackResponse
)
def get_feedback(
    feedback_id: int,
    db: Session = Depends(get_db)
):
    feedback = db.query(Feedback).filter(
        Feedback.id == feedback_id
    ).first()

    if not feedback:
        raise HTTPException(
            status_code=404,
            detail="Feedback não encontrado."

        )

    return feedback