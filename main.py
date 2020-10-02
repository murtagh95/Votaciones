from clases import *
from sistemaVotacion import SistemaVotacion
from random import randint


FECHA = Fecha(15, 5, 2019)


DIRECCIONES = [
	# BARRIO LA BLORIA
	Direccion("Rawson", 0, "La Gloria"),
	Direccion("Puerto San Jose", 0, "La Gloria"),
	Direccion("Bahía Aguirre", 0, "La Gloria"),
	Direccion("Puerto Concepción", 0, "La Gloria"),
	Direccion("Bahía Ushuaia", 0, "La Gloria"),
	Direccion("Puerto año nuevo", 0, "La Gloria"),
	# BARRIO FUCH
	Direccion("Laguna Palena", 0, "Fuch"),
	Direccion("Lago Hermoso", 0, "Fuch"),
	Direccion("Lago Correntoso", 0, "Fuch"),
	Direccion("Laguna de la esquina", 0, "Fuch"),
	Direccion("Laguna de la Niña Encantada", 0, "Fuch"),
	Direccion("Laguna del Toro", 0, "Fuch"),
	# BARRIO LA ESTANZUELA
	Direccion("Telteca", 0, "La Estanzuela"),
	Direccion("Tilcara", 0, "La Estanzuela"),
	Direccion("Payer", 0, "La Estanzuela"),
	Direccion("Mapuche", 0, "La Estanzuela"),
	Direccion("Trenque Lauquen", 0, "La Estanzuela"),
	Direccion("Yupanqui", 0, "La Estanzuela"),
	# BARRIO GOBERNADOR BENEGAS
	Direccion("Artigas", 0, "Gobernador Benegas"),
	Direccion("Roffo A.", 0, "Gobernador Benegas"),
	Direccion("Hilario Cuadros", 0, "Gobernador Benegas"),
	Direccion("Gargilo", 0, "Gobernador Benegas"),
	Direccion("Feliciani", 0, "Gobernador Benegas"),
	Direccion("Alfaro", 0, "Gobernador Benegas"),
	# BARRIO SAN VICENTE
	Direccion("Dique Tulumaya", 0, "San Vicente"),
	Direccion("Chile", 0, "San Vicente"),
	Direccion("El Nihuil", 0, "San Vicente"),
	Direccion("Alpatacal", 0, "San Vicente"),
	Direccion("Los Jacatanda", 0, "San Vicente"),
	Direccion("Las Casuarinas", 0, "San Vicente"),
	# BARRIO VILLA HIPÓDROMO
	Direccion("Pismata", 0, "Villa Hipódromo"),
	Direccion("El volcan", 0, "Villa Hipódromo"),
	Direccion("El Vergel", 0, "Villa Hipódromo"),
	Direccion("Cosquín", 0, "Villa Hipódromo"),
	Direccion("Pedernera", 0, "Villa Hipódromo"),
	Direccion("América", 0, "Villa Hipódromo"),
]

NOMBRES = [
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
]

APELLIDOS =[
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
]

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
	for i in range(500):
		# Declaro variables con valores aleatorios
		nombre = NOMBRES[randint(0,(len(NOMBRES)-1))]
		apellido = APELLIDOS[randint(0,(len(APELLIDOS)-1))]
		direccion = DIRECCIONES[randint(0,(len(DIRECCIONES)-1))]
		padron = Padron(randint(0, 1000), controlBarrio(direccion.barrio), FECHA)
		direccion.num = randint(0, 1000)

		# Cargo el array con el objeto
		votantes.append(Votante(nombre, apellido, randint(5000000, 48000000), randint(18, 99), direccion, False, padron))
	
	return votantes

votantes = generarVotantes()

# for votante in votantes:
# 	print(votante)
# 	print("-------------------------")


def generarCandidatos():
	listas = []
	tadeo = Candidato("Tadeo", "Zalazar", 35025896, 35, DIRECCIONES[21], False, controlBarrio(DIRECCIONES[21].barrio), "Intendente", True)
	listas.append(Lista(PartidoPolitico("Cambia Mendoza"), 503, tadeo))

	andrea  = Candidato("Andrea", "Blandini", 55078897, 55, DIRECCIONES[26], False, controlBarrio(DIRECCIONES[26].barrio), "Intendente", True)
	listas.append(Lista(PartidoPolitico("Eleguí Mendoza"), 43, andrea))

	hector = Candidato("Héctor", "Fresina", 29634785, 30, DIRECCIONES[15], False, controlBarrio(DIRECCIONES[15].barrio), "Intendente", True)
	listas.append(Lista(PartidoPolitico("FIT"), 786, hector))

	leonardo = Candidato("Leonardo", "Verdini", 47568932, 45, DIRECCIONES[30], False, controlBarrio(DIRECCIONES[30].barrio), "Intendente", True)
	listas.append(Lista(PartidoPolitico("Protectora"), 105, leonardo))

	return listas

listas = generarCandidatos()

# for lista in listas:
# 	print(lista)
# 	print("------------------")



def generarVotos():
	listaVotos = []
	numAlAzar = 0
	for i in range(500):
		numAlAzar = randint(1,3)
		if numAlAzar == 1:
			listaVotos.append(Voto(listas[randint(0,3)],True, False, False))
		elif numAlAzar == 2:
			listaVotos.append(Voto(listas[randint(0,3)],False, True, False))
		else:
			listaVotos.append(Voto(listas[randint(0,3)],False, False, True))
	
	return listaVotos

listaVotos = generarVotos()
# for lista in listaVotos:
# 	print(lista)
# 	print("------------------")

sistemaVotacion = SistemaVotacion(listas, votantes, FECHA, listaVotos)

print(sistemaVotacion.controlVotaciones())
sistemaVotacion.controlVotaciones()
print(sistemaVotacion.estadoDeVotos)

for can
