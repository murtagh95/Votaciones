from clases.votante import Votante

class Candidato(Votante):
    def __init__(self, nombre, apellido, dni, edad, direccion, voto, padronElectoral, puesto, titular):
        super().__init__(nombre, apellido, dni, edad, direccion, voto, padronElectoral)
        self.puesto = puesto
        self.titular = titular

    def __str__(self):
        return  super().__str__() + "\nPuesto: {}, titular?: {}".format(
            self.puesto,
            self.titular,
            )
    

