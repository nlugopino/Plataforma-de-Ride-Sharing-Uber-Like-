from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi.responses import FileResponse

from reportlab.pdfgen import canvas

import os

from app.database.connection import SessionLocal

from app.models.servicio import Servicio

from app.template.comprobante_estandar import (
    ComprobanteEstandar
)

from app.template.comprobante_premium import (
    ComprobantePremium
)

from app.template.comprobante_corporativo import (
    ComprobanteCorporativo
)

router = APIRouter()


def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.get(
    "/comprobante/{servicio_id}/{tipo}"
)

@router.get(
    "/comprobante/{servicio_id}/{tipo}"
)
def generar_comprobante(
    servicio_id: int,
    tipo: str,
    db: Session = Depends(get_db)
):

    servicio = db.query(Servicio).filter(
        Servicio.id == servicio_id
    ).first()

    generador = None

    if tipo == "estandar":

        generador = ComprobanteEstandar()

    elif tipo == "premium":

        generador = ComprobantePremium()

    elif tipo == "corporativo":

        generador = ComprobanteCorporativo()

    comprobante = generador.generar(servicio)

    servicio.tipo_comprobante = tipo

    db.commit()

    nombre_pdf = (f"comprobante_{servicio.id}.pdf")

    ruta_pdf = os.path.join("temp",nombre_pdf)

    os.makedirs("temp", exist_ok=True)

    pdf = canvas.Canvas(ruta_pdf)

    pdf.setFont("Helvetica-Bold", 16)

    pdf.drawString(100,800,"COMPROBANTE DE SERVICIO")

    pdf.setFont("Helvetica", 12)

    pdf.drawString(100,760,f"Origen: {comprobante['datos']['origen']}")

    pdf.drawString(100,730,f"Destino: {comprobante['datos']['destino']}")

    pdf.drawString(100,700,f"Total: ${comprobante['total']}")

    pdf.drawString(100,670,f"Detalle: {comprobante['extra']}")

    pdf.save()

    return FileResponse(
        path=ruta_pdf,
        filename=nombre_pdf,
        media_type='application/pdf'
    )