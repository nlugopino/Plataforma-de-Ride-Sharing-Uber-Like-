from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.connection import Base

class Vehiculo(Base):

    __tablename__ = "vehiculos"

    id = Column(Integer, primary_key=True, index=True)

    tipo_vehiculo = Column(String)
    placa = Column(String)
    modelo = Column(Integer)
    cilindraje = Column(Integer)

    conductor_id = Column(Integer, ForeignKey("conductores.id"), unique=True)

    conductor = relationship(
        "Conductor",
        back_populates="vehiculo"
    )