from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class Pasajero(Base):

    __tablename__ = "pasajeros"

    id = Column(Integer, primary_key=True, index=True)
    documento = Column(String, unique=True)
    nombre = Column(String)
    correo = Column(String)
    telefono = Column(String)
    puntos = Column(Integer, default=0)
    nivel = Column(String, default="Bronce")
    tema = Column(
        String,
        default="claro"
    )