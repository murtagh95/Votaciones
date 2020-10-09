from funciones import DIRECCIONES, controlBarrio
from clases import Lista, PartidoPolitico, Candidato

def crearLista300():
    lista300 = []
    # Creo todos los candidatos de la lista 300 y los agrego a lista que engloba las 4 listas
	lista300.append(Candidato(
        "Tadeo", 
        "Zalazar", 
        35025896, 
        35,
        DIRECCIONES[20], 
        False, 
        controlBarrio(DIRECCIONES[20].barrio), 
        "Intendente", 
        True
    ))
	lista300.append(Candidato("Fabricio", "Cuaranta", 49025894, 44, DIRECCIONES[19], False, controlBarrio(DIRECCIONES[19].barrio), "Consejal", True))
	lista300.append(Candidato("Noelia", "Santino", 49825894, 37, DIRECCIONES[18], False, controlBarrio(DIRECCIONES[18].barrio), "Consejal", True))
	lista300.append(Candidato("Leonardo", "Mostrángelo", 44325894, 30, DIRECCIONES[17], False, controlBarrio(DIRECCIONES[17].barrio), "Consejal", True))
	lista300.append(Candidato("María", "Molina", 4905894, 30, DIRECCIONES[16], False, controlBarrio(DIRECCIONES[16].barrio), "Consejal", True))
	lista300.append(Candidato("Juan", "Guevara", 49024764, 38, DIRECCIONES[15], False, controlBarrio(DIRECCIONES[15].barrio), "Consejal", True))
	lista300.append(Candidato("Florencia", "Castro", 36825894, 32, DIRECCIONES[14], False, controlBarrio(DIRECCIONES[14].barrio), "Consejal", True))
	lista300.append(Candidato("Emilio", "Zieba", 44025894, 36, DIRECCIONES[13], False, controlBarrio(DIRECCIONES[13].barrio), "Consejal", False))
	lista300.append(Candidato("Claudia", "Mercado", 49025894, 29, DIRECCIONES[12], False, controlBarrio(DIRECCIONES[12].barrio), "Consejal", False))
	lista300.append(Candidato("Érica", "Caciamani", 49025176, 48, DIRECCIONES[11], False, controlBarrio(DIRECCIONES[11].barrio), "Consejal", False))
    # lista300 = [tadeo, consejal1, consejal2, consejal3, consejal4, consejal5, consejal6, consejal7, consejal8, consejal9]
    return Lista(PartidoPolitico("Cambia Mendoza"), 300, lista300)
