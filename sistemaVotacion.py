from clases import *


class SistemaVotacion():
    def __init__(self, listas, votantes, fecha, votos):
        self.listas = listas
        self.votantes = votantes
        self.fecha = fecha
        self.votos = votos
        self.estadoDeVotos = None
        self.listaPorcentaje = None

    def controlVotaciones(self):
        votosBlancos = 0
        votosImpugnados = 0
        votosValidos = 0
        for voto in self.votos:
            if voto.blanco:
                votosBlancos += 1
            elif voto.impugnado:
                votosImpugnados += 1
            else:
                votosValidos += 1
        self.estadoDeVotos = {
            "Blancos" : votosBlancos,
            "Impugnados" : votosImpugnados,
            "Validos" : votosValidos,
        }
    
    def porcentajeCandidato(self):
        listaPorcentaje = [0,0,0,0]
        
        for voto in self.votos:
            if voto.valido:
                if voto.lista.numLista == self.listas[0].numLista:
                    listaPorcentaje[0] += 1
                elif voto.lista.numLista == self.listas[1].numLista:
                    listaPorcentaje[1] += 1
                elif voto.lista.numLista == self.listas[2].numLista:
                    listaPorcentaje[2] += 1
                else:
                    listaPorcentaje[3] += 1
        
        for i in range(len(listaPorcentaje)):
            listaPorcentaje[i] = ((listaPorcentaje[i] * 100) / len(self.votos))


        self.listaPorcentaje = listaPorcentaje
    
    def mostrarPorcentajeCandidatos(self):

        
    def buscarGanador(self, lista):
        pass
