from tkinter import *


def controlVotos(raiz, sistemaVotacion, COLOR_FONDO):
    
    # Creo una segunda ventana
    segundaVentana = Toplevel(raiz)
    segundaVentana.resizable(0,0)
    segundaVentana.geometry("250x150")
    segundaVentana.config(bg=COLOR_FONDO)

    miFrame1 = Frame(segundaVentana, bg=COLOR_FONDO)
    miFrame1.pack()

    # -----------MUESTRO LOS VOTOS EN BLANCO---------------------
    BlancosLabel = Label(miFrame1, text="Blancos", bg=COLOR_FONDO)
    BlancosLabel.grid(row=1, column=0, padx=10, pady=10)

    textoLabel = sistemaVotacion.estadoDeVotos["Blancos"]
    BlancosValorLabel = Label(miFrame1, text=textoLabel, bg=COLOR_FONDO)
    BlancosValorLabel.grid(row=2, column=0, padx=10, pady=10)

    # -----------MUESTRO LOS VOTOS IMPUGNADOS---------------------
    impugnadosLabel = Label(miFrame1, text="Impugnados", bg=COLOR_FONDO)
    impugnadosLabel.grid(row=1, column=1, padx=10, pady=10)
    
    textoLabel = sistemaVotacion.estadoDeVotos["Impugnados"]
    BlancosValorLabel = Label(miFrame1, text=textoLabel, bg=COLOR_FONDO)
    BlancosValorLabel.grid(row=2, column=1, padx=10, pady=10)

    # -----------MUESTRO LOS VOTOS VALIDOS---------------------
    validosLabel = Label(miFrame1, text="Validos", bg=COLOR_FONDO)
    validosLabel.grid(row=1, column=2, padx=10, pady=10)
    
    textoLabel = sistemaVotacion.estadoDeVotos["Validos"]
    BlancosValorLabel = Label(miFrame1, text=textoLabel, bg=COLOR_FONDO)
    BlancosValorLabel.grid(row=2, column=2, padx=10, pady=10)
