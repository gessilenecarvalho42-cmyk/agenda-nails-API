from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class Manicure(Base):
    __tablename__ = "tb_manicure"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    active = Column(Boolean, default=True, nullable=False)

    appointments = relationship(
        "Appointment",
        back_populates="manicure"
    )