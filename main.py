from funciones.generarCandidatos import GenerarCandidatos
from funciones.generarVotantes import GenerarVotantes, FECHA
from funciones.generarVotos import GenerarVotos, cambiarPorcNoVotantes
from clases.sistemaVotacion import SistemaVotacion
from grafica.venPrincipal import ventanaPrincipal


# Genero los datos
votantes = GenerarVotantes()
listas = GenerarCandidatos()
listaVotos = GenerarVotos(votantes, listas)
sistemaVotacion = SistemaVotacion(listas, votantes, FECHA, listaVotos)
sistemaVotacion.porcentajeCandidato()

# LLamo a la funciòn grafica
ventanaPrincipal(sistemaVotacion)

    

