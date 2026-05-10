from app.models.reporte_incidente import ReporteIncidente

class ReporteBuilder:

    def __init__(self):
        self.reporte = ReporteIncidente()

    def set_servicio(self, servicio_id):
        self.reporte.servicio_id = servicio_id
        return self

    def set_tipo(self, tipo):
        self.reporte.tipo_incidente = tipo
        return self

    def set_descripcion(self, descripcion):
        self.reporte.descripcion = descripcion
        return self

    def set_estado(self):
        self.reporte.estado = "pendiente"
        return self

    def build(self):
        return self.reporte