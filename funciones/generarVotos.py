# Importo modulos propios
from clases.voto import Voto
# Importo librerias externas
from random import randint, choice


# Genero que cantidad de personas que no votaran
LISTA_NO_VOTANTES = (15, 16, 17, 18, 19, 20, 50)
porc_no_votantes = choice(LISTA_NO_VOTANTES)

def cambiarPorcNoVotantes():
	global porc_no_votantes

	azar =  choice(LISTA_NO_VOTANTES)

	porc_no_votantes = azar
	
	return azar

def candidatosAzar():
	lista = [0, 1, 2, 3]
	listaAlAzar = []

	# Genero una lista del 0 al 3 desordenada
	for _ in range(4):
		num = choice(lista)
		listaAlAzar.append(num)
		lista.remove(num)
	
	return [listaAlAzar[0]] * 45 + [listaAlAzar[1]] * 35 + [listaAlAzar[2]] * 15 + [listaAlAzar[3]] * 5

def GenerarVotos(votantes, listas, porcNoVotantes=porc_no_votantes):
    listaVotos = []
    # Lista que permitira crear con desigualdad los votos
    # impugnados = 1%, blacos = 10%, validos = 89%
    my_list = [2] * 1 + [1] * 10 + [3] * 89
    numAlAzar = 0   
    
    # Convierto el porcentaje de no votantes a un nº
    cantidadNoVotantes = (porcNoVotantes * len(votantes)) / 100
    contador = 0

    # Genero un arrey para que las votaciones a una determinada lista no sea pareja
    elejirLista = candidatosAzar()
    for votante in votantes:
		# Variable para que los no votantes sean al azars
        azar = choice([1, 2, 2])
        if azar == 1 and contador < cantidadNoVotantes:
            contador+= 1
        else:
            votante.voto = True
            numAlAzar = choice(my_list)
            if numAlAzar == 1:
                listaVotos.append(Voto(listas[choice(elejirLista)], blanco= True))
            elif numAlAzar == 2:
                listaVotos.append(Voto(listas[choice(elejirLista)], impugnado = True))
            else:
                listaVotos.append(Voto(listas[choice(elejirLista)], valido = True))

    return listaVotos
    
