from clases import *


class SistemaVotacion():
    def __init__(self, listas, votantes, fecha, votos):
        self.listas = listas
        self.votantes = votantes
        self.fecha = fecha
        self.votos = votos
        self.estadoDeVotos = None
        self.listaPorcentaje = []

    def controlVotaciones(self):
        # Declaro variables auxiliares
        votosBlancos = 0
        votosImpugnados = 0
        votosValidos = 0
        
        # Recorro los votos y controlo como fue el voto
        for voto in self.votos:
            if voto.blanco:
                votosBlancos += 1
            elif voto.impugnado:
                votosImpugnados += 1
            else:
                votosValidos += 1
        
        # Asigno un diccionario con los valores correspondientes
        self.estadoDeVotos = {
            "Blancos" : votosBlancos,
            "Impugnados" : votosImpugnados,
            "Validos" : votosValidos,
        }
    
    def porcentajeCandidato(self):
        listaPorcentaje = [0,0,0,0]
        
        # Recorro los votos
        for voto in self.votos:
            # Controlo que solo se sumen los votos validos
            if voto.valido:
                # Controlo a que lista corresponde el voto
                if voto.lista.numLista == self.listas[0].numLista:
                    listaPorcentaje[0] += 1
                elif voto.lista.numLista == self.listas[1].numLista:
                    listaPorcentaje[1] += 1
                elif voto.lista.numLista == self.listas[2].numLista:
                    listaPorcentaje[2] += 1
                else:
                    listaPorcentaje[3] += 1
        
        # Cambio el nº de votos por porcentaje
        for i in range(len(listaPorcentaje)):
            listaPorcentaje[i] = ((listaPorcentaje[i] * 100) / len(self.votos))
            listaPorcentaje[i] = round(listaPorcentaje[i], 2)
        
        # Asigno el valor al atributo del objeto
        self.listaPorcentaje = listaPorcentaje
    
    def mostrarPorcentajeCandidatos(self):
        # Controlamos si se puede mostrar, ya que depende de ya haber calculado el porcentajeCandidato
        try:
            for i in range(len(self.listas)):
                print("El candidato: ", self.listas[i].candidatos.nombre, "obtuvo", self.listaPorcentaje[i], "% votos.")
        except:
            print("Error, para mostrar primero se debe realizar el calculo")
        
    def buscarGanador(self):
        # Defino variable aux
        listaGanadora = []

        # Verifico los candidatos con más del 40% de votos
        for i in range(len(self.listaPorcentaje)):
            if self.listaPorcentaje[i] > 40:
                listaGanadora.append(self.listas[i])

        # Controlo si ningun candidato saco mas del 40%
        if len(listaGanadora) == False:
            mayor = 0
            indiceMayor = 0
            indiceSegundoMayor = 0

            # Busco el mayor porcentaje
            for i in range(len(self.listaPorcentaje)):
                if self.listaPorcentaje[i] > mayor:
                    mayor = self.listaPorcentaje[i]
                    indiceMayor = i
            # Busco el segundo mayor porcentaje
            mayor = 0
            for i in range(len(self.listaPorcentaje)):
                if self.listaPorcentaje[i] > mayor and self.listaPorcentaje[i] != self.listaPorcentaje[indiceMayor]:
                    mayor = self.listaPorcentaje[i]
                    indiceSegundoMayor = i
            
                
        return """Los 2 candidatos que tendran que ir a la segunda vuelta son: 
                    -Candidao: {}, con {}% de votos.
                    -Candidao: {}, con {}% de votos.""".format(
            self.listas[indiceMayor].candidatos.nombre,
            self.listaPorcentaje[indiceMayor],
            self.listas[indiceSegundoMayor].candidatos.nombre,
            self.listaPorcentaje[indiceSegundoMayor],
            )

 
    def imprimirNoVotantes(self):
        for votante in self.votantes:
            if not(votante.voto):
                print("El siguiente votante no voto:")
                print(votante)


        

