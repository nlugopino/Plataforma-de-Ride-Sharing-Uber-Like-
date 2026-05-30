import copy


class UbicacionPrototype:

    def clonar(self, ubicacion):

        return copy.deepcopy(
            ubicacion
        )