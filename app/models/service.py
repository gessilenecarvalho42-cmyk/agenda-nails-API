from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from app.database import Base


class Service(Base):
    __tablename__ = "tb_servico"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(200), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    duration = Column(String(50), nullable=False)

    appointments = relationship(
        "Appointment",
        back_populates="service"
    )
