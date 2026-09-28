from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.database import Base


class Notification(Base):
    __tablename__ = "tb_notificacao"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(50), nullable=False)
    message = Column(String(255), nullable=False)
    sent_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    read = Column(Boolean, default=False, nullable=False)

    appointment_id = Column(
        Integer,
        ForeignKey("tb_agendamento.id"),
        nullable=False
    )

    appointment = relationship(
        "Appointment",
        back_populates="notifications"
    )