from funciones import generarVotantes, generarVotos, generarCandidatos, FECHA
from sistemaVotacion import SistemaVotacion

# Genero los datos
votantes = generarVotantes()
listas = generarCandidatos()
listaVotos = generarVotos(votantes, listas)


sistemaVotacion = SistemaVotacion(listas, votantes, FECHA, listaVotos)

# Calculamos cuantos votos fueron blancos/impugnados/validos
sistemaVotacion.controlVotaciones()
# Mostramos las cantidades de votos en blancos/impugnados/validos
print(sistemaVotacion.estadoDeVotos)

sistemaVotacion.porcentajeCandidato()
sistemaVotacion.mostrarPorcentajeCandidatos()

print(sistemaVotacion.buscarGanador())

# Imprimimos los votantes que no asistieron a la votación
# sistemaVotacion.imprimirNoVotantes()

