from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "tb_usuario"

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String(20), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(30), nullable=False, default="CLIENTE")
    client_id = Column(
        Integer,
        ForeignKey("tb_cliente.id"),
        nullable=True,
        unique=True
    )

    client = relationship("Client", back_populates="user")