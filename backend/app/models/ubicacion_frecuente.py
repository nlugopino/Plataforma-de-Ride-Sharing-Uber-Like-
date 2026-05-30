from sqlalchemy import Column, Integer, String, ForeignKey

from app.database.connection import Base


class UbicacionFrecuente(Base):

    __tablename__ = "ubicaciones_frecuentes"

    id = Column(Integer, primary_key=True)

    tipo = Column(String)

    direccion = Column(String)

    pasajero_id = Column(
        Integer,
        ForeignKey("pasajeros.id")
    )