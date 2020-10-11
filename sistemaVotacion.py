from clases import *
from funciones import PORC_NO_VOTANTES


class SistemaVotacion():
    def __init__(self, listas, votantes, fecha, votos):
        self.listas = listas
        self.votantes = votantes
        self.fecha = fecha
        self.votos = votos
        self.estadoDeVotos = None
        self.listaPorcentaje = None
        self.listaCantidadVotos = None
        self.votacionValida = False

        # Ejecuto 2 métodos fundamentales
        self.controlVotaciones()
        self.calcularVotacionValida()

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
        # Creo un diccionario cuyas keys seran el nº de lista de cada Partido politico
        lista1 = {
            self.listas[0].numLista : 0,
            self.listas[1].numLista : 0,
            self.listas[2].numLista : 0,
            self.listas[3].numLista : 0,
        }
        
        # Recorro los votos
        for voto in self.votos:
            # Controlo que solo se sumen los votos validos
            if voto.valido:
                # Controlo a que lista corresponde el voto
                lista1[voto.lista.numLista] += 1
        
        self.listaCantidadVotos = lista1
        listaPorcentaje = lista1.copy()

        # Cambio el nº de votos por porcentaje
        for clave in lista1.keys():
            listaPorcentaje[clave] = ((listaPorcentaje[clave] * 100) / self.estadoDeVotos["Validos"])
            listaPorcentaje[clave] = round(listaPorcentaje[clave], 2)
        
        # Asigno el valor al atributo del objeto
        self.listaPorcentaje = listaPorcentaje
    
    def mostrarPorcentajeCandidatos(self):
        # Controlamos si se puede mostrar, ya que depende de ya haber calculado el porcentajeCandidato
        try:
            print("Candidatos\t|\tVotos\t|\tPorcentaje")
            for i in range(len(self.listas)):
                print("{}\t\t|\t{}\t|\t{}%.".format(
                    self.listas[i].candidatos[0].nombre,
                    self.listaCantidadVotos[self.listas[i].numLista],
                    self.listaPorcentaje[self.listas[i].numLista]
                ))
        except:
            print("Error, para mostrar primero se debe realizar el calculo")
        
    def buscarGanador(self):
        # Defino variable aux
        listaGanadora = []
        contador = 0

        # Verifico los candidatos con más del 40% de votos
        for clave in self.listaPorcentaje.keys():
            if self.listaPorcentaje[clave] > 40:
                listaGanadora.append(self.listas[contador])
                listaGanadora.append(self.listaPorcentaje[clave])
            contador += 1

        # Controlo si ningun candidato saco mas del 40%
        if len(listaGanadora) == False:
            contador = 0
            mayor = 0
            indiceMayor = 0
            indiceSegundoMayor = 0

            # Busco el mayor porcentaje
            for clave in self.listaPorcentaje.keys():
                if self.listaPorcentaje[clave] > mayor:
                    mayor = self.listaPorcentaje[clave]
                    indiceMayor = contador
                contador += 1

            # Busco el segundo mayor porcentaje
            mayor = 0
            contador = 0
            # Cambio el indice mayor por una clave
            claveMayor =  self.listas[indiceMayor].numLista

            for clave in self.listaPorcentaje.keys():
                if self.listaPorcentaje[clave] > mayor and self.listaPorcentaje[clave] != self.listaPorcentaje[claveMayor]:
                    mayor = self.listaPorcentaje[clave]
                    indiceSegundoMayor = contador
                contador += 1
            
            return [
                self.listas[indiceMayor],
                self.listaPorcentaje[claveMayor],
                self.listas[indiceSegundoMayor],
                self.listaPorcentaje[self.listas[indiceSegundoMayor].numLista],
            ]
        else:
            return listaGanadora

    def calcularConsejales(self):
        # Arrey que contendra los consejales ganadores
        consejalesGanadores = []
        contador = 0

        # Recorro el atributo que almacena la cantidad de votos por cada lista
        for clave in self.listaCantidadVotos.keys():
            cantidad = self.listaCantidadVotos[clave] // 60
            for j in range(cantidad):
                consejalesGanadores.append({
                    "candidato" : self.listas[contador].candidatos[j+1],
                    "lista" : self.listas[contador]
                    })
            
            contador = contador + 1

        
        return consejalesGanadores

    def calcularVotacionValida(self, porcen = PORC_NO_VOTANTES):
        # Convierto el porcentaje de no votantes a un nº
        cantidadNoVotantes = (porcen * len(self.votantes)) / 100

        suma = cantidadNoVotantes + self.estadoDeVotos["Blancos"] + self.estadoDeVotos["Impugnados"]
        porcentaje = (suma * 100) / len(self.votantes)
        
        if porcentaje <= 50:
            self.votacionValida = True
        else :
            self.votacionValida = False

       
