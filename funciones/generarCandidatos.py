# Importo modulos propios
from clases.candidato import Candidato
from clases.lista import Lista
from clases.partidoPolitico import PartidoPolitico
from funciones.generarVotantes import DIRECCIONES, controlBarrio


def GenerarCandidatos():
    lista = []
    lista300 = []
    lista301 = []
    lista302 = []
    lista222 = []
    # Creo todos los candidatos de la lista 300 
    lista300.append(Candidato("Tadeo", "Zalazar", 35025896, 35, DIRECCIONES[20], False, controlBarrio(DIRECCIONES[20].barrio), "Intendente", True))
    lista300.append(Candidato("Fabricio", "Cuaranta", 49025894, 44, DIRECCIONES[19], False, controlBarrio(DIRECCIONES[19].barrio), "Consejal", True))
    lista300.append(Candidato("Noelia", "Santino", 49825894, 37, DIRECCIONES[18], False, controlBarrio(DIRECCIONES[18].barrio), "Consejal", True))
    lista300.append(Candidato("Leonardo", "Mostrángelo", 44325894, 30, DIRECCIONES[17], False, controlBarrio(DIRECCIONES[17].barrio), "Consejal", True))
    lista300.append(Candidato("María", "Molina", 4905894, 30, DIRECCIONES[16], False, controlBarrio(DIRECCIONES[16].barrio), "Consejal", True))
    lista300.append(Candidato("Juan", "Guevara", 49024764, 38, DIRECCIONES[15], False, controlBarrio(DIRECCIONES[15].barrio), "Consejal", True))
    lista300.append(Candidato("Florencia", "Castro", 36825894, 32, DIRECCIONES[14], False, controlBarrio(DIRECCIONES[14].barrio), "Consejal", True))
    lista300.append(Candidato("Emilio", "Zieba", 44025894, 36, DIRECCIONES[13], False, controlBarrio(DIRECCIONES[13].barrio), "Consejal", False))
    lista300.append(Candidato("Claudia", "Mercado", 49025894, 29, DIRECCIONES[12], False, controlBarrio(DIRECCIONES[12].barrio), "Consejal", False))
    lista300.append(Candidato("Érica", "Caciamani", 49025176, 48, DIRECCIONES[11], False, controlBarrio(DIRECCIONES[11].barrio), "Consejal", False))
    lista.append(Lista(PartidoPolitico("Cambia Mendoza"), 300, lista300))

    # Creo todos los candidatos de la lista 301 
    lista301.append(Candidato("Héctor", "Fresina", 29634785, 30, DIRECCIONES[10], False, controlBarrio(DIRECCIONES[10].barrio), "Intendente", True))
    lista301.append(Candidato("Manuel", "Tello", 49561894, 44, DIRECCIONES[9], False, controlBarrio(DIRECCIONES[9].barrio), "Consejal", True))
    lista301.append(Candidato("Martina", "Rivero", 59825794, 37, DIRECCIONES[8], False, controlBarrio(DIRECCIONES[8].barrio), "Consejal", True))
    lista301.append(Candidato("Leonardo", "Gómez", 44325801, 30, DIRECCIONES[7], False, controlBarrio(DIRECCIONES[7].barrio), "Consejal", True))
    lista301.append(Candidato("Jorgelina", "Luna", 4709994, 30, DIRECCIONES[6], False, controlBarrio(DIRECCIONES[6].barrio), "Consejal", True))
    lista301.append(Candidato("Raúl", "Zamarian", 46021722, 38, DIRECCIONES[5], False, controlBarrio(DIRECCIONES[5].barrio), "Consejal", True))
    lista301.append(Candidato("José", "Filippis", 36825794, 32, DIRECCIONES[4], False, controlBarrio(DIRECCIONES[4].barrio), "Consejal", True))
    lista301.append(Candidato("Lorena", "Quiroga", 30014894, 52, DIRECCIONES[3], False, controlBarrio(DIRECCIONES[3].barrio), "Consejal", False))
    lista301.append(Candidato("Daiana", "Lopéz", 30007794, 48, DIRECCIONES[2], False, controlBarrio(DIRECCIONES[2].barrio), "Consejal", False))
    lista301.append(Candidato("Celia", "Segal", 29221171, 47, DIRECCIONES[1], False, controlBarrio(DIRECCIONES[1].barrio), "Consejal", False))
    lista.append(Lista(PartidoPolitico("Frente de izquierda"), 301, lista301))

    # Creo todos los candidatos de la lista 302 
    lista302.append(Candidato("Andrea", "Blandini", 55078897, 55, DIRECCIONES[26], False, controlBarrio(DIRECCIONES[26].barrio), "Intendente", True))
    lista302.append(Candidato("Gabriela", "Malina", 49565894, 44, DIRECCIONES[25], False, controlBarrio(DIRECCIONES[25].barrio), "Consejal", True))
    lista302.append(Candidato("Cristian", "Ramo", 59825894, 37, DIRECCIONES[24], False, controlBarrio(DIRECCIONES[24].barrio), "Consejal", True))
    lista302.append(Candidato("Néstor", "Roy", 44325811, 30, DIRECCIONES[23], False, controlBarrio(DIRECCIONES[23].barrio), "Consejal", True))
    lista302.append(Candidato("Rosa", "Villarruel", 4909994, 30, DIRECCIONES[22], False, controlBarrio(DIRECCIONES[22].barrio), "Consejal", True))
    lista302.append(Candidato("Nicolás", "Mercado", 49021722, 38, DIRECCIONES[21], False, controlBarrio(DIRECCIONES[21].barrio), "Consejal", True))
    lista302.append(Candidato("Nora", "Llaver", 36825994, 32, DIRECCIONES[27], False, controlBarrio(DIRECCIONES[27].barrio), "Consejal", True))
    lista302.append(Candidato("Jorge", "Villegas", 30025894, 35, DIRECCIONES[28], False, controlBarrio(DIRECCIONES[28].barrio), "Consejal", False))
    lista302.append(Candidato("Claudia", "Cejas", 30005894, 39, DIRECCIONES[29], False, controlBarrio(DIRECCIONES[29].barrio), "Consejal", False))
    lista302.append(Candidato("Federico", "Vilches", 29025171, 52, DIRECCIONES[30], False, controlBarrio(DIRECCIONES[30].barrio), "Consejal", False))
    lista.append(Lista(PartidoPolitico("Eleguí Mendoza"), 302, lista302))

    # Creo todos los candidatos de la lista 222 
    lista222.append(Candidato("Leonardo", "Verdini", 47568932, 45, DIRECCIONES[31], False, controlBarrio(DIRECCIONES[31].barrio), "Intendente", True))
    lista222.append(Candidato("Mauro", "Cesar", 49521824, 34, DIRECCIONES[32], False, controlBarrio(DIRECCIONES[32].barrio), "Consejal", True))
    lista222.append(Candidato("Maria", "Fozzatti", 50825094, 57, DIRECCIONES[33], False, controlBarrio(DIRECCIONES[33].barrio), "Consejal", True))
    lista222.append(Candidato("Mario", "Riccio", 4325801, 35, DIRECCIONES[34], False, controlBarrio(DIRECCIONES[34].barrio), "Consejal", True))
    lista222.append(Candidato("Ana", "Leguizamon", 4709094, 34, DIRECCIONES[35], False, controlBarrio(DIRECCIONES[35].barrio), "Consejal", True))
    lista222.append(Candidato("Hugo", "Vargas", 46021700, 36, DIRECCIONES[36], False, controlBarrio(DIRECCIONES[36].barrio), "Consejal", True))
    lista222.append(Candidato("Erica", "Gonzales", 36820094, 31, DIRECCIONES[37], False, controlBarrio(DIRECCIONES[37].barrio), "Consejal", True))
    lista222.append(Candidato("Mauricio", "Molina", 30014194, 55, DIRECCIONES[38], False, controlBarrio(DIRECCIONES[38].barrio), "Consejal", False))
    lista222.append(Candidato("Lorena", "Alvarez", 30007764, 58, DIRECCIONES[39], False, controlBarrio(DIRECCIONES[39].barrio), "Consejal", False))
    lista222.append(Candidato("Mariano", "Ortiz", 29221172, 57, DIRECCIONES[40], False, controlBarrio(DIRECCIONES[40].barrio), "Consejal", False))
    lista.append(Lista(PartidoPolitico("Protectora"), 222, lista222))

    return lista
