class PartidoPolitico(object):
    def __init__(nombre):
        self.nombre = nombre


class Persona(object):
    def __init__(nombre, apellido, dni, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad


class Fecha(object):
    def __init__(dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio

class Padron(object):
    def __init__(numMesa, lugar, seccion, fecha):
        self.numMesa = numMesa
        self.lugar = lugar
        self.seccion = seccion
        self.fecha = fecha


class Votatne(Persona):
    def __init__(voto, padronElectoral):
        self.voto = voto
        self.padronElectoral = padronElectoral



class Candidato(Votante):
    def __init__(titulo, puesto, titular):
        self.titulo = titulo
        self.puesto = puesto
        self.titular = titular


class Lista(object):
    def __init__(parPolitico, numLista, candidato):
        self.parPolitico = parPolitico
        self.numLista = numLista
        self.candidato = candidato


class Voto(object):
    def __init__(lista, blanco, impugnado, valido):
        self.lista = lista
        self.blanco = blanco
        self.impugnado = impugnado
        self.valido = valido
    

class SistemaVotacion(object):
    def __init__(listas, votantes, fecha, votos):
        self.listas = listas
        self.votantes = votantes
        self.fecha = fecha
        self.votos = votos




