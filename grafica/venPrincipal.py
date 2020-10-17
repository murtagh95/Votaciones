# Importo modulos propios
from grafica.verConsejales import verConsejales 
from grafica.verGanador import verGanador
from grafica.verNoVotantes import verNoVotantes
from grafica.verVotantes import verVotantes
from grafica.imprimirVotante import imprimirVotante
from grafica.buscarPorDNI import buscarPorDNI
from grafica.controlVotos import controlVotos
from grafica.votosCandidatos import votosCandidatos
from funciones.generarCandidatos import GenerarCandidatos
from funciones.generarVotantes import GenerarVotantes, FECHA
from funciones.generarVotos import GenerarVotos, cambiarPorcNoVotantes
from clases.sistemaVotacion import SistemaVotacion
# Importo librerias externas
from tkinter import *

# ------CONSTANTES---------
COLOR_FONDO = "#8eedd2"
COLOR_TITULO = "#03076b"
COLOR_RED = "#f26e50"


def reiniciar(raiz):
    global sistemaVotacion, listaVotos, votantes
    nuevoNumNoVotante = cambiarPorcNoVotantes()

    votantes = GenerarVotantes()
    listas = GenerarCandidatos()
    listaVotos = GenerarVotos(votantes, listas, nuevoNumNoVotante)
    sistemaVotacion = SistemaVotacion(listas, votantes, FECHA, listaVotos)
    sistemaVotacion.porcentajeCandidato()
    
    sistemaVotacion.calcularVotacionValida(nuevoNumNoVotante)    
    
    raiz.destroy()
    ventanaPrincipal(sistemaVotacion)


def ventanaPrincipal(sistemaVotacion):
    # Creo la ventana   
    raiz = Tk()
    raiz.title("Votaciónes")
    raiz.geometry("400x480")
    raiz.resizable(0,0)
    raiz.config(bg=COLOR_FONDO)


    miFrame1 = Frame(raiz, bg=COLOR_FONDO)
    miFrame1.pack()

    bienvenidaLabel = Label(miFrame1, text="Bienvenido al programa para controlar las votaciones", bg=COLOR_FONDO, fg=COLOR_TITULO)
    bienvenidaLabel.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    if sistemaVotacion.votacionValida:
        eleguirLabel = Label(miFrame1, text="¿Que deseas hacer?", bg=COLOR_FONDO)
        eleguirLabel.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        botonVerPorVotos = Button(miFrame1, text="Ver porcentaje de votos Blancos/Impugnados/Validos", command=lambda:controlVotos(raiz, sistemaVotacion, COLOR_FONDO), bg=COLOR_RED)
        botonVerPorVotos.config(padx="5", pady="5")
        botonVerPorVotos.grid(row=2, column=0)

        botonVerVotos = Button(miFrame1, text="Ver porcentaje de votos por lista", command=lambda:votosCandidatos(raiz, sistemaVotacion, COLOR_FONDO), bg=COLOR_RED)
        botonVerVotos.config(padx="5", pady="5")
        botonVerVotos.grid(row=3, column=0)

        botonVerGanador = Button(miFrame1, text="Ver ganador de votaciones", command=lambda:verGanador(raiz, sistemaVotacion, COLOR_FONDO), bg=COLOR_RED)
        botonVerGanador.config(padx="5", pady="5")
        botonVerGanador.grid(row=4, column=0)

        botonVerConsejales = Button(miFrame1, text="Ver consejales que ganaron", command=lambda:verConsejales(raiz, sistemaVotacion, COLOR_FONDO), bg=COLOR_RED)
        botonVerConsejales.config(padx="5", pady="5")
        botonVerConsejales.grid(row=5, column=0)

        botonVerNoVotantes = Button(miFrame1, text="Ver personas que no votaron", command=lambda:verNoVotantes(raiz, sistemaVotacion, COLOR_FONDO), bg=COLOR_RED)
        botonVerNoVotantes.config(padx="5", pady="5")
        botonVerNoVotantes.grid(row=6, column=0)

        botonVerNoVotantes = Button(miFrame1, text="Ver total de votantes", command=lambda:verVotantes(raiz, sistemaVotacion, COLOR_FONDO), bg=COLOR_RED)
        botonVerNoVotantes.config(padx="5", pady="5")
        botonVerNoVotantes.grid(row=7, column=0)

        botonVerNoVotantes = Button(miFrame1, text="Buscar persona por el DNI", command=lambda:buscarPorDNI(raiz, sistemaVotacion, COLOR_FONDO), bg=COLOR_RED)
        botonVerNoVotantes.config(padx="5", pady="5")
        botonVerNoVotantes.grid(row=8, column=0)

        Label(miFrame1, bg=COLOR_FONDO).grid(row=9, column=0)
        Label(miFrame1, bg=COLOR_FONDO).grid(row=10, column=0)
        Label(miFrame1, bg=COLOR_FONDO).grid(row=11, column=0)
        Label(miFrame1, bg=COLOR_FONDO).grid(row=12, column=0)
        Label(miFrame1, bg=COLOR_FONDO).grid(row=13, column=0)

    else:
        eleguirLabel = Label(miFrame1, text="Votación invalida, por favor realizar una nueva votación", bg=COLOR_FONDO)
        eleguirLabel.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    botonReiniciar = Button(miFrame1, text="Reiniciar las votaciones", command=lambda : reiniciar(raiz), bg=COLOR_RED)
    botonReiniciar.config(padx="5", pady="5")
    botonReiniciar.grid(row=14, column=0)



    raiz.mainloop()
