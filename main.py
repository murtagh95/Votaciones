from funciones import generarVotantes, generarVotos, generarCandidatos, FECHA, cambiarPorcNoVotantes
from sistemaVotacion import SistemaVotacion
from tkinter import *
from ventanasGraficas import *

# Genero los datos
votantes = generarVotantes()
listas = generarCandidatos()
listaVotos = generarVotos(votantes, listas)
sistemaVotacion = SistemaVotacion(listas, votantes, FECHA, listaVotos)
sistemaVotacion.porcentajeCandidato()

def reiniciar(raiz):
    global sistemaVotacion, listaVotos, votantes
    nuevoNumNoVotante = cambiarPorcNoVotantes()

    votantes = generarVotantes()
    listaVotos = generarVotos(votantes, listas, nuevoNumNoVotante)
    sistemaVotacion = SistemaVotacion(listas, votantes, FECHA, listaVotos)
    sistemaVotacion.porcentajeCandidato()
    
    sistemaVotacion.calcularVotacionValida(nuevoNumNoVotante)    
    
    raiz.destroy()
    ventanaPrincipal()
    

def ventanaPrincipal():
    # Creo la ventana   
    raiz = Tk()
    raiz.title("Votaciónes")
    raiz.geometry("400x480")
    raiz.resizable(0,0)
    raiz.config(bg="#8eedd2")


    miFrame1 = Frame(raiz, bg="#8eedd2")
    miFrame1.pack()

    bienvenidaLabel = Label(miFrame1, text="Bienvenido al programa para controlar las votaciones", bg="#8eedd2", fg="#0a732a")
    bienvenidaLabel.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    if sistemaVotacion.votacionValida:
        eleguirLabel = Label(miFrame1, text="¿Que deseas hacer?", bg="#8eedd2")
        eleguirLabel.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        botonVerPorVotos = Button(miFrame1, text="Ver porcentaje de votos Blancos/Impugnados/Validos", command=lambda:controlVotos(raiz, sistemaVotacion), bg="#f26e50")
        botonVerPorVotos.config(padx="5", pady="5")
        botonVerPorVotos.grid(row=2, column=0)

        botonVerVotos = Button(miFrame1, text="Ver porcentaje de votos por lista", command=lambda:votosCandidatos(raiz, sistemaVotacion), bg="#f26e50")
        botonVerVotos.config(padx="5", pady="5")
        botonVerVotos.grid(row=3, column=0)

        botonVerGanador = Button(miFrame1, text="Ver ganador de votaciones", command=lambda:verGanador(raiz, sistemaVotacion), bg="#f26e50")
        botonVerGanador.config(padx="5", pady="5")
        botonVerGanador.grid(row=4, column=0)

        botonVerConsejales = Button(miFrame1, text="Ver consejales que ganaron", command=lambda:verConsejales(raiz, sistemaVotacion), bg="#f26e50")
        botonVerConsejales.config(padx="5", pady="5")
        botonVerConsejales.grid(row=5, column=0)

        botonVerNoVotantes = Button(miFrame1, text="Ver personas que no votaron", command=lambda:verNoVotantes(raiz, sistemaVotacion), bg="#f26e50")
        botonVerNoVotantes.config(padx="5", pady="5")
        botonVerNoVotantes.grid(row=6, column=0)

        botonVerNoVotantes = Button(miFrame1, text="Ver total de votantes", command=lambda:verVotantes(raiz, sistemaVotacion), bg="#f26e50")
        botonVerNoVotantes.config(padx="5", pady="5")
        botonVerNoVotantes.grid(row=7, column=0)

        botonVerNoVotantes = Button(miFrame1, text="Buscar persona por el DNI", command=lambda:buscarPorDNI(raiz, sistemaVotacion), bg="#f26e50")
        botonVerNoVotantes.config(padx="5", pady="5")
        botonVerNoVotantes.grid(row=8, column=0)

        Label(miFrame1, bg="#8eedd2").grid(row=9, column=0)
        Label(miFrame1, bg="#8eedd2").grid(row=10, column=0)
        Label(miFrame1, bg="#8eedd2").grid(row=11, column=0)
        Label(miFrame1, bg="#8eedd2").grid(row=12, column=0)
        Label(miFrame1, bg="#8eedd2").grid(row=13, column=0)

    else:
        eleguirLabel = Label(miFrame1, text="Votación invalida, por favor realizar una nueva votación", bg="#8eedd2")
        eleguirLabel.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    botonReiniciar = Button(miFrame1, text="Reiniciar las votaciones", command=lambda : reiniciar(raiz), bg="#f26e50")
    botonReiniciar.config(padx="5", pady="5")
    botonReiniciar.grid(row=14, column=0)



    raiz.mainloop()


ventanaPrincipal()

