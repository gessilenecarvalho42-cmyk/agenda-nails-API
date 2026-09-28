from app.database import Base  # ajuste a importação do seu Base conforme seu projeto
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship


class Feedback(Base):
  __tablename__ = "feedbacks"

  id = Column(Integer, primary_key=True, index=True)
  rating = Column(Integer, nullable=False)  # ex: nota de 1 a 5
  comment = Column(Text, nullable=True)  # comentário opcional

  # Chave estrangeira ligando ao agendamento (tb_agendamento.id)
  appointment_id = Column(
      Integer, ForeignKey("tb_agendamento.id"), nullable=False, unique=True
  )

  # Relacionamento de volta com a tabela de agendamento
  appointment = relationship("Appointment", back_populates="feedback")