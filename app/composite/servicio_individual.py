from composite.componente import ComponenteServicio

# Servicio individual (Leaf)
class ServicioIndividual(ComponenteServicio):

    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo

    def calcular_costo(self):
        print(f"[Composite] Servicio {self.nombre}: {self.costo}")
        return self.costo