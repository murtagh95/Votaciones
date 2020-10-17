from clases.persona import Persona


class Votante(Persona):
    def __init__(self, nombre, apellido, dni, edad, direccion, voto, padronElectoral):
        super().__init__(nombre, apellido, dni, edad, direccion)
        self.voto = voto
        self.padronElectoral = padronElectoral

    def __str__(self):
        return "Nombre: {}, Apellido: {}, DNI: {}, Edad: {}, Dirección: {} {}/{}, Voto: {}, \n---Padron Electoral---\n {}".format(
            self.nombre,
            self.apellido,
            self.dni,
            self.edad,
            self.direccion.calle,
            self.direccion.num,
            self.direccion.barrio,
            self.voto,
            self.padronElectoral,
            )
