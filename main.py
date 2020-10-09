from funciones import generarVotantes, generarVotos, generarCandidatos, FECHA
from sistemaVotacion import SistemaVotacion
from tkinter import *

# Genero los datos
votantes = generarVotantes()
listas = generarCandidatos()
listaVotos = generarVotos(votantes, listas)


# Creo la ventana   
raiz = Tk()
raiz.title("Votaciónes")
raiz.geometry("400x400")
raiz.resizable(0,0)
raiz.config(bg="#8eedd2")


miFrame1 = Frame(raiz, bg="#8eedd2")
miFrame1.pack()

bienvenidaLabel = Label(miFrame1, text="Bienvenido al programa para controlar las votaciones", bg="#8eedd2", fg="#0a732a")
bienvenidaLabel.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

eleguirLabel = Label(miFrame1, text="¿Que deseas hacer?", bg="#8eedd2")
eleguirLabel.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

botonVerPorVotos = Button(miFrame1, text="Ver porcentaje de votos Blancos/Impugnados/Validos", bg="#f26e50")
botonVerPorVotos.grid(row=2, column=0)

raiz.mainloop()


sistemaVotacion = SistemaVotacion(listas, votantes, FECHA, listaVotos)

# Mostramos las cantidades de votos en blancos/impugnados/validos
print(sistemaVotacion.estadoDeVotos)

sistemaVotacion.porcentajeCandidato()
sistemaVotacion.mostrarPorcentajeCandidatos()

print(sistemaVotacion.buscarGanador())

# Imprimimos los votantes que no asistieron a la votación
# sistemaVotacion.imprimirNoVotantes()
# print(len(sistemaVotacion.votos))

sistemaVotacion.calcularConsejales()
