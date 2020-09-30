
class PartidoPolitico():
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return "El partido politico se llama {}".format(self.nombre)


class Persona():
    def __init__(self, nombre, apellido, dni, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad


class Fecha():
    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio

class Padron():
    def __init__(self, numMesa, lugar, seccion, fecha):
        self.numMesa = numMesa
        self.lugar = lugar
        self.seccion = seccion
        self.fecha = fecha
    
    def __str__(self):
        return "Número mesa: {}, Lugar: {}, Seccion: {}, fecha: {}/{}/{}".format(
            self.numMesa,
            self.lugar,
            self.seccion,
            self.fecha.dia,
            self.fecha.mes,
            self.fecha.anio,
            )


class Votante(Persona):
    def __init__(self, nombre, apellido, dni, edad, voto, padronElectoral):
        super().__init__(nombre, apellido, dni, edad)
        self.voto = voto
        self.padronElectoral = padronElectoral

    def __str__(self):
        return "Nombre: {}, Apellido: {}, DNI: {}, Edad: {}, Voto: {}, \n---Padron Electoral---\n {}".format(
            self.nombre,
            self.apellido,
            self.dni,
            self.edad,
            self.voto,
            self.padronElectoral,
            )

class Candidato(Votante):
    def __init__(self, nombre, apellido, dni, edad, voto, padronElectoral, titulo, puesto, titular):
        super().__init__(nombre, apellido, dni, edad, voto, padronElectoral)
        self.titulo = titulo
        self.puesto = puesto
        self.titular = titular

    def __str__(self):
        return  super().__str__() + "\nTitulo: {}, Puesto: {}, titular?: {}".format(
            self.titulo,
            self.puesto,
            self.titular,
            )
    


class Lista():
    def __init__(self, parPolitico, numLista, candidatos):
        self.parPolitico = parPolitico
        self.numLista = numLista
        self.candidatos = candidatos

    def __str__(self):
        return  "Partido Politico: {}, Número Lista: {}, Candidato: \n{}".format(
            self.parPolitico.nombre,
            self.numLista,
            self.candidatos,
            )


class Voto():
    def __init__(self, lista, blanco, impugnado, valido):
        self.lista = lista
        self.blanco = blanco
        self.impugnado = impugnado
        self.valido = valido
    

class SistemaVotacion():
    def __init__(self, listas, votantes, fecha, votos):
        self.listas = listas
        self.votantes = votantes
        self.fecha = fecha
        self.votos = votos




