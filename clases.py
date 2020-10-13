class PartidoPolitico():
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return "El partido politico se llama {}".format(self.nombre)


class Direccion():
    def __init__(self, calle, num, barrio):
        self.calle = calle
        self.num = num
        self.barrio = barrio


class Persona():
    def __init__(self, nombre, apellido, dni, edad, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad
        self.direccion = direccion



class Fecha():
    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio

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
    


class Lista():
    def __init__(self, parPolitico, numLista, candidatos):
        self.parPolitico = parPolitico
        self.numLista = numLista
        self.candidatos = candidatos
    
    def mostrarCandidatos(self):
        consejales = ""
        for candidato in self.candidatos:
            consejales += "-{} {} .Candidato al puesto {}, titular {}\n".format(candidato.nombre, candidato.apellido, candidato.puesto, candidato.titular)
        
        return consejales

    def __str__(self):
        return  "Partido Politico: {}, Número Lista: {}, Candidato: \n{}".format(
            self.parPolitico.nombre,
            self.numLista,
            self.mostrarCandidatos(),
            )


class Voto():
    def __init__(self, lista, blanco = False, impugnado = False, valido = False):
        self.lista = lista
        self.blanco = blanco
        self.impugnado = impugnado
        self.valido = valido
    
    def __str__(self):
        return  "Voto a lista: {}, \n¿Voto blanco?: {}, \n¿Voto impugnado?: {}, \n¿Voto valido?: {},".format(
            self.lista,
            self.blanco,
            self.impugnado,
            self.valido,
            )

