from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.types import Date
from app.models.database import Base


class Registro(Base):
    __tablename__ = "registro"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), unique=True, index=True)
    horario_consulta = Column(DateTime)
    