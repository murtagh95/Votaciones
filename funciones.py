from clases import *
from random import randint, choice


FECHA = Fecha(15, 5, 2019)
CANTIDAD_VOTANTES = 500

DIRECCIONES = (
	# BARRIO LA BLORIA
	Direccion("Rawson", 0, "La Gloria"),
	Direccion("Puerto San Jose", 0, "La Gloria"),
	Direccion("Bahía Aguirre", 0, "La Gloria"),
	Direccion("Puerto Concepción", 0, "La Gloria"),
	Direccion("Bahía Ushuaia", 0, "La Gloria"),
	Direccion("Puerto año nuevo", 0, "La Gloria"),
	Direccion("Vélez Sarfield", 0, "La Gloria"),
	# BARRIO FUCH
	Direccion("Laguna Palena", 0, "Fuch"),
	Direccion("Lago Hermoso", 0, "Fuch"),
	Direccion("Lago Correntoso", 0, "Fuch"),
	Direccion("Laguna de la esquina", 0, "Fuch"),
	Direccion("Laguna de la Niña Encantada", 0, "Fuch"),
	Direccion("Laguna del Toro", 0, "Fuch"),
	Direccion("Lago Pulmari", 0, "Fuch"),
	# BARRIO LA ESTANZUELA
	Direccion("Telteca", 0, "La Estanzuela"),
	Direccion("Tilcara", 0, "La Estanzuela"),
	Direccion("Payer", 0, "La Estanzuela"),
	Direccion("Mapuche", 0, "La Estanzuela"),
	Direccion("Trenque Lauquen", 0, "La Estanzuela"),
	Direccion("Yupanqui", 0, "La Estanzuela"),
	Direccion("Pte Arturo Illia", 0, "La Estanzuela"),
	# BARRIO GOBERNADOR BENEGAS
	Direccion("Artigas", 0, "Gobernador Benegas"),
	Direccion("Roffo A.", 0, "Gobernador Benegas"),
	Direccion("Hilario Cuadros", 0, "Gobernador Benegas"),
	Direccion("Gargilo", 0, "Gobernador Benegas"),
	Direccion("Feliciani", 0, "Gobernador Benegas"),
	Direccion("Alfaro", 0, "Gobernador Benegas"),
	Direccion("Tudela", 0, "Gobernador Benegas"),
	# BARRIO SAN VICENTE
	Direccion("Dique Tulumaya", 0, "San Vicente"),
	Direccion("Chile", 0, "San Vicente"),
	Direccion("El Nihuil", 0, "San Vicente"),
	Direccion("Alpatacal", 0, "San Vicente"),
	Direccion("Los Jacatanda", 0, "San Vicente"),
	Direccion("Las Casuarinas", 0, "San Vicente"),
	Direccion("Dique los Nihuiles", 0, "San Vicente"),
	# BARRIO VILLA HIPÓDROMO
	Direccion("Pismata", 0, "Villa Hipódromo"),
	Direccion("El volcan", 0, "Villa Hipódromo"),
	Direccion("El Vergel", 0, "Villa Hipódromo"),
	Direccion("Cosquín", 0, "Villa Hipódromo"),
	Direccion("Pedernera", 0, "Villa Hipódromo"),
	Direccion("América", 0, "Villa Hipódromo"),
	Direccion("La Plata", 0, "Villa Hipódromo")
)

NOMBRES = (
	"Nicolas",
	"Jose",
	"Manuel",
	"Francisco",
	"Ciro",
	"Maria",
	"Noemi",
	"Lucia",
	"Teresa",
	"Natalia",
	"Camila",
	"Thalia",
	"Alexis",
	"Sol",
	"Lucrecio"
)


APELLIDOS =(
	"Catalano",
	"Salimeni",
	"Coria",
	"Figueroa",
	"Muratore",
	"Ortiz",
	"Perez",
	"Gonzales",
	"Matus",
	"Perez",
	"Echegaray",
	"Gomez",
	"Ruiz",
	"Manna",
	"Brizuela"
)


def controlBarrio(barrio):
	""" Función que permite asignar una escuela para la votación segun el barrio de residencia """

	if barrio == "La Gloria":
		return "Esc Padre Pedro Arce"

	elif barrio == "Fuch":
		return "Esc Reyes Catolico"

	elif barrio == "La Estanzuela":
		return "Esc Profesor Geronimo Sosa"

	elif barrio == "Gobernador Benegas":
		return "Esc Misiones"

	elif barrio == "San Vicente":
		return "Esc DR. Americo Cali"

	else:
		return "Esc Victoria Ocampo"

def generarVotantes():
	votantes = []
	for i in range(CANTIDAD_VOTANTES):
		# Declaro variables con valores aleatorios
		direccion = choice(DIRECCIONES)
		padron = Padron(randint(0, 1000), controlBarrio(direccion.barrio), FECHA)
		direccion.num = randint(0, 1000)

		# Cargo el array con el objeto
		votantes.append(Votante(
			choice(NOMBRES),
			choice(APELLIDOS), 
			randint(5000000, 48000000), 
			randint(18, 99), 
			direccion, 
			False, 
			padron)
		)
	
	return votantes


def generarCandidatos():
    lista = []
    lista300 = []
    lista301 = []
    lista302 = []
    lista222 = []
    # Creo todos los candidatos de la lista 300 y los agrego a lista que engloba las 4 listas
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

    # Creo todos los candidatos de la lista 301 y los agrego a lista que engloba las 4 listas
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

    # Creo todos los candidatos de la lista 302 y los agrego a lista que engloba las 4 listas
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

    # Creo todos los candidatos de la lista 222 y los agrego a lista que engloba las 4 listas
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

def generarVotos(votantes, listas):
	listaVotos = []
	# Lista que permitira crear con desigualdad los votos
	# impugnados = 1%, blacos = 10%, validos = 89%
	my_list = [2] * 1 + [1] * 10 + [3] * 89
	numAlAzar = 0

	# Genero que cantidad de personas que no votaran
	porcNoVotantes = choice([15, 16, 17, 18, 19, 20])
	cantidadNoVotantes = (porcNoVotantes * len(votantes)) / 100
	contador = 0
	for votante in votantes:
		azar = choice([1, 2, 2, 2])
		if azar == 1 and contador <= cantidadNoVotantes:
			contador+= 1
		else:
			votante.voto = True
			numAlAzar = choice(my_list)
			if numAlAzar == 1:
				listaVotos.append(Voto(listas[randint(0,3)],True, False, False))
			elif numAlAzar == 2:
				listaVotos.append(Voto(listas[randint(0,3)],False, True, False))
			else:
				listaVotos.append(Voto(listas[randint(0,3)],False, False, True))
	
	return listaVotos
