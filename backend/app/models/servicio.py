from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

from app.database.connection import Base


class Servicio(Base):

    __tablename__ = "servicios"

    id = Column(Integer, primary_key=True, index=True)
    uuid_servicio = Column(
        String,
        unique=True,
        default=lambda: str(uuid.uuid4())
    )
    direccion_origen = Column(String)
    direccion_destino = Column(String)
    tipo_servicio = Column(String)
    distancia_km = Column(Float)
    valor_oferta = Column(Float)
    estado = Column(String, default="pendiente")
    metodo_pago = Column(String, nullable=True)
    fecha_solicitud = Column(DateTime, default=datetime.utcnow)
    fecha_finalizacion = Column(DateTime, nullable=True)
    calificacion = Column(Integer, nullable=True)
    comentario_calificacion = Column(String, nullable=True)
    descuento_aplicado = Column(Float, default=0)
    promociones = Column(String, nullable=True)
    total_final = Column(Float, default=0)
    pasajero_id = Column(
        Integer,
        ForeignKey("pasajeros.id")
    )
    conductor_id = Column(
        Integer,
        ForeignKey("conductores.id"),
        nullable=True
    )
    pasajero = relationship("Pasajero")
    conductor = relationship("Conductor")