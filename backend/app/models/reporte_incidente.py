from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func

from app.database.connection import Base

class ReporteIncidente(Base):

    __tablename__ = "reportes_incidentes"

    id = Column(Integer, primary_key=True, index=True)

    servicio_id = Column(
        Integer,
        ForeignKey("servicios.id"),
        unique=True
    )

    tipo_incidente = Column(String)

    descripcion = Column(String)

    estado = Column(String, default="pendiente")

    fecha_reporte = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )