from tkinter import *


def verConsejales(raiz, sistemaVotacion, COLOR_FONDO):
    consejales = sistemaVotacion.calcularConsejales()
    contador = 0
    
    # Creo una segunda ventana
    segundaVentana = Toplevel(raiz)
    segundaVentana.resizable(0,0)
    segundaVentana.geometry("400x400")
    segundaVentana.config(bg=COLOR_FONDO)

    miFrame1 = Frame(segundaVentana, bg=COLOR_FONDO)
    miFrame1.pack()

    Label(miFrame1, text="Los consejales ganadores son:", bg=COLOR_FONDO).grid(row=1, column=0, columnspan=6, padx=10, pady=10)
    
    Label(miFrame1, text="Nombre", bg=COLOR_FONDO).grid(row=2, column=0, padx=10, pady=10)
    Label(miFrame1, text="Apellido", bg=COLOR_FONDO).grid(row=2, column=1, padx=10, pady=10)
    Label(miFrame1, text="Puesto", bg=COLOR_FONDO).grid(row=2, column=2, padx=10, pady=10)
    Label(miFrame1, text="Partido Politico", bg=COLOR_FONDO).grid(row=2, column=3, padx=10, pady=10)
    Label(miFrame1, text="Lista", bg=COLOR_FONDO).grid(row=2, column=4, padx=10, pady=10)

    for consejal in consejales:

        textoLabel = consejal["candidato"].nombre
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3+contador, column=0, padx=10, pady=10)

        textoLabel = consejal["candidato"].apellido
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3+contador, column=1, padx=10, pady=10)

        textoLabel = consejal["candidato"].puesto
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3+contador, column=2, padx=10, pady=10)

        textoLabel = consejal["lista"].parPolitico.nombre
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3+contador, column=3, padx=10, pady=10)

        textoLabel = consejal["lista"].numLista
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3+contador, column=4, padx=10, pady=10)

        contador += 1
      