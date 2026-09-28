from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Client(Base):
    __tablename__ = "tb_cliente"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    consent_whatsapp = Column(Boolean, default=False, nullable=False)
    active = Column(Boolean, default=True, nullable=False)

    appointments = relationship("Appointment", back_populates="client")
    user = relationship("User", back_populates="client", uselist=False, cascade="all, delete-orphan")
