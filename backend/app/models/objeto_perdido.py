from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)

from datetime import datetime

from app.database.connection import Base


class ObjetoPerdido(Base):

    __tablename__ = "objetos_perdidos"

    id = Column(
        Integer,
        primary_key=True
    )

    tipo = Column(String)

    descripcion = Column(String)

    fecha_reporte = Column(
        DateTime,
        default=datetime.utcnow
    )

    servicio_id = Column(
        Integer,
        ForeignKey("servicios.id"),
        unique=True
    )