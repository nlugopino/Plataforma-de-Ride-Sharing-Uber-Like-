from app.composite.componente import ComponenteServicio

# Composite
class PaqueteServicios(ComponenteServicio):

    def __init__(self, nombre):
        self.nombre = nombre
        self.servicios = []

    def agregar(self, servicio):
        self.servicios.append(servicio)

    def calcular_costo(self):
        print(f"[Composite] Calculando paquete: {self.nombre}")

        total = 0
        for servicio in self.servicios:
            total += servicio.calcular_costo()

        print(f"[Composite] Total paquete {self.nombre}: {total}")
        return total