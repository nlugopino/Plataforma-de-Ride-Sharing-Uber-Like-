import os

from reportlab.pdfgen import canvas

from app.builders.reporte_conductor_builder import (ReporteConductorBuilder)


class ReporteMensualBuilder(
    ReporteConductorBuilder
):

    def __init__(
        self,
        conductor,
        servicios,
        mes,
        anio
    ):

        self.conductor = conductor

        self.servicios = servicios

        self.mes = mes

        self.anio = anio

        os.makedirs(
            "reportes",
            exist_ok=True
        )

        self.ruta = (
            f"reportes/"
            f"reporte_{mes}_{anio}.pdf"
        )

        self.pdf = canvas.Canvas(
            self.ruta
        )

        self.y = 760

    def agregar_titulo(self):

        self.pdf.setFont(
            "Helvetica-Bold",
            18
        )

        self.pdf.drawString(
            50,
            800,
            "Reporte mensual"
        )

    def agregar_conductor(self):

        self.pdf.setFont(
            "Helvetica",
            12
        )

        self.pdf.drawString(
            50,
            770,
            f"Conductor: {self.conductor.nombre}"
        )

    def agregar_servicios(self):

        self.y = 720

        for servicio in self.servicios:

            total = (
                servicio.valor_oferta
                +
                (servicio.propina or 0)
            )

            self.pdf.drawString(
                50,
                self.y,
                f"{servicio.direccion_origen}"
                f" -> "
                f"{servicio.direccion_destino}"
                f"  ${total}"
            )

            self.y -= 20

    def agregar_totales(self):

        total = sum(
            s.valor_oferta
            +
            (s.propina or 0)
            for s in self.servicios
        )

        self.pdf.drawString(
            50,
            self.y - 20,
            f"TOTAL GANADO: ${total}"
        )

    def obtener_pdf(self):

        self.pdf.save()

        return self.ruta