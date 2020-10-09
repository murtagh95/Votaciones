from funciones import DIRECCIONES, controlBarrio
from clases import Lista, PartidoPolitico, Candidato

def crearLista222():
    # Creo todos los candidatos de la lista 222 y los agrego a lista que engloba las 4 listas
	leonardo = Candidato("Leonardo", "Verdini", 47568932, 45, DIRECCIONES[31], False, controlBarrio(DIRECCIONES[31].barrio), "Intendente", True)
    consejal1 = Candidato("Mauro", "Cesar", 49521824, 34, DIRECCIONES[32], False, controlBarrio(DIRECCIONES[32].barrio), "Consejal", True)
	consejal2 = Candidato("Maria", "Fozzatti", 50825094, 57, DIRECCIONES[33], False, controlBarrio(DIRECCIONES[33].barrio), "Consejal", True)
	consejal3 = Candidato("Mario", "Riccio", 4325801, 35, DIRECCIONES[34], False, controlBarrio(DIRECCIONES[34].barrio), "Consejal", True)
	consejal4 = Candidato("Ana", "Leguizamon", 4709094, 34, DIRECCIONES[35], False, controlBarrio(DIRECCIONES[35].barrio), "Consejal", True)
	consejal5 = Candidato("Hugo", "Vargas", 46021700, 36, DIRECCIONES[36], False, controlBarrio(DIRECCIONES[36].barrio), "Consejal", True)
	consejal6 = Candidato("Erica", "Gonzales", 36820094, 31, DIRECCIONES[37], False, controlBarrio(DIRECCIONES[37].barrio), "Consejal", True)
	consejal7 = Candidato("Mauricio", "Molina", 30014194, 55, DIRECCIONES[38], False, controlBarrio(DIRECCIONES[38].barrio), "Consejal", False)
	consejal8 = Candidato("Lorena", "Alvarez", 30007764, 58, DIRECCIONES[39], False, controlBarrio(DIRECCIONES[39].barrio), "Consejal", False)
	consejal9 = Candidato("Mariano", "Ortiz", 29221172, 57, DIRECCIONES[40], False, controlBarrio(DIRECCIONES[40].barrio), "Consejal", False)
    lista222 = [leonardo, consejal1, consejal2, consejal3, consejal4, consejal5, consejal6, consejal7, consejal8, consejal9]
	return Lista(PartidoPolitico("Protectora"), 222, lista222)
