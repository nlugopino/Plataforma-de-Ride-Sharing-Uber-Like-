class Viaje:

    def __init__(self):
        self.distancia = None
        self.tarifa = None
        self.propina = None
        self.total = None

    def __str__(self):
        return f"Viaje(distancia={self.distancia}, tarifa={self.tarifa}, propina={self.propina}, total={self.total})"