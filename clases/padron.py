
class Padron():
    def __init__(self, numMesa, lugar, fecha):
        self.numMesa = numMesa
        self.lugar = lugar
        self.fecha = fecha
    
    def __str__(self):
        return "Número mesa: {}, Lugar: {}, fecha: {}/{}/{}".format(
            self.numMesa,
            self.lugar,
            self.fecha.dia,
            self.fecha.mes,
            self.fecha.anio,
            )
