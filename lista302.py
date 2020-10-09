from funciones import DIRECCIONES, controlBarrio
from clases import Lista, PartidoPolitico, Candidato

def crearLista302():
    # Creo todos los candidatos de la lista 302 y los agrego a lista que engloba las 4 listas
	andrea  = Candidato("Andrea", "Blandini", 55078897, 55, DIRECCIONES[26], False, controlBarrio(DIRECCIONES[26].barrio), "Intendente", True)
    consejal1 = Candidato("Gabriela", "Malina", 49565894, 44, DIRECCIONES[25], False, controlBarrio(DIRECCIONES[25].barrio), "Consejal", True)
	consejal2 = Candidato("Cristian", "Ramo", 59825894, 37, DIRECCIONES[24], False, controlBarrio(DIRECCIONES[24].barrio), "Consejal", True)
	consejal3 = Candidato("Néstor", "Roy", 44325811, 30, DIRECCIONES[23], False, controlBarrio(DIRECCIONES[23].barrio), "Consejal", True)
	consejal4 = Candidato("Rosa", "Villarruel", 4909994, 30, DIRECCIONES[22], False, controlBarrio(DIRECCIONES[22].barrio), "Consejal", True)
	consejal5 = Candidato("Nicolás", "Mercado", 49021722, 38, DIRECCIONES[21], False, controlBarrio(DIRECCIONES[21].barrio), "Consejal", True)
	consejal6 = Candidato("Nora", "Llaver", 36825994, 32, DIRECCIONES[27], False, controlBarrio(DIRECCIONES[27].barrio), "Consejal", True)
	consejal7 = Candidato("Jorge", "Villegas", 30025894, 35, DIRECCIONES[28], False, controlBarrio(DIRECCIONES[28].barrio), "Consejal", False)
	consejal8 = Candidato("Claudia", "Cejas", 30005894, 39, DIRECCIONES[29], False, controlBarrio(DIRECCIONES[29].barrio), "Consejal", False)
	consejal9 = Candidato("Federico", "Vilches", 29025171, 52, DIRECCIONES[30], False, controlBarrio(DIRECCIONES[30].barrio), "Consejal", False)
    lista302 = [andrea, consejal1, consejal2, consejal3, consejal4, consejal5, consejal6, consejal7, consejal8, consejal9]
	return Lista(PartidoPolitico("Eleguí Mendoza"), 302, lista302)

