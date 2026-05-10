from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.connection import Base

class Conductor(Base):

    __tablename__ = "conductores"

    id = Column(Integer, primary_key=True, index=True)
    documento = Column(String, unique=True)
    nombre = Column(String)
    correo = Column(String)
    telefono = Column(String)

    vehiculo = relationship(
        "Vehiculo",
        back_populates="conductor",
        uselist=False
    )