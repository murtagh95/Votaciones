from funciones import DIRECCIONES, controlBarrio
from clases import Lista, PartidoPolitico, Candidato

def crearLista301():
    # Creo todos los candidatos de la lista 301 y los agrego a lista que engloba las 4 listas
	hector = Candidato("Héctor", "Fresina", 29634785, 30, DIRECCIONES[10], False, controlBarrio(DIRECCIONES[10].barrio), "Intendente", True)
    consejal1 = Candidato("Manuel", "Tello", 49561894, 44, DIRECCIONES[9], False, controlBarrio(DIRECCIONES[9].barrio), "Consejal", True)
	consejal2 = Candidato("Martina", "Rivero", 59825794, 37, DIRECCIONES[8], False, controlBarrio(DIRECCIONES[8].barrio), "Consejal", True)
	consejal3 = Candidato("Leonardo", "Gómez", 44325801, 30, DIRECCIONES[7], False, controlBarrio(DIRECCIONES[7].barrio), "Consejal", True)
	consejal4 = Candidato("Jorgelina", "Luna", 4709994, 30, DIRECCIONES[6], False, controlBarrio(DIRECCIONES[6].barrio), "Consejal", True)
	consejal5 = Candidato("Raúl", "Zamarian", 46021722, 38, DIRECCIONES[5], False, controlBarrio(DIRECCIONES[5].barrio), "Consejal", True)
	consejal6 = Candidato("José", "Filippis", 36825794, 32, DIRECCIONES[4], False, controlBarrio(DIRECCIONES[4].barrio), "Consejal", True)
	consejal7 = Candidato("Lorena", "Quiroga", 30014894, 52, DIRECCIONES[3], False, controlBarrio(DIRECCIONES[3].barrio), "Consejal", False)
	consejal8 = Candidato("Daiana", "Lopéz", 30007794, 48, DIRECCIONES[2], False, controlBarrio(DIRECCIONES[2].barrio), "Consejal", False)
	consejal9 = Candidato("Celia", "Segal", 29221171, 47, DIRECCIONES[1], False, controlBarrio(DIRECCIONES[1].barrio), "Consejal", False)
    lista301 = [hector, consejal1, consejal2, consejal3, consejal4, consejal5, consejal6, consejal7, consejal8, consejal9]
	return Lista(PartidoPolitico("Frente de izquierda"), 301, lista301)