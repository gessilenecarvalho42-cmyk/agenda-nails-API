from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Appointment(Base):
    __tablename__ = "tb_agendamento"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    status = Column(String(50), default="CONFIRMADO", nullable=False)

    client_id = Column(Integer, ForeignKey("tb_cliente.id"), nullable=False)
    manicure_id = Column(Integer, ForeignKey("tb_manicure.id"), nullable=False)
    service_id = Column(Integer, ForeignKey("tb_servico.id"), nullable=False)

    client = relationship("Client", back_populates="appointments")
    manicure = relationship("Manicure", back_populates="appointments")
    service = relationship("Service", back_populates="appointments")
    feedback = relationship("Feedback", back_populates="appointment", uselist=False, cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="appointment", cascade="all, delete-orphan")
