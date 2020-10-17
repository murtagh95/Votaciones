# Importo modulos propios
from clases.direccion import Direccion
from clases.padron import Padron
from clases.votante import Votante
from clases.fecha import Fecha
# Importo librerias externas
from random import choice, randint

#------DEFINO CONSTANTES------- 
CANTIDAD_VOTANTES = 500
FECHA = Fecha(15, 5, 2019)

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

# ------DEFINO FUNCIONES---------
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


def GenerarVotantes():
	votantes = []
	for _ in range(CANTIDAD_VOTANTES):
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
