from tkinter import *


def votosCandidatos(raiz, sistemaVotacion, COLOR_FONDO):
    
    # Creo una segunda ventana
    segundaVentana = Toplevel(raiz)
    segundaVentana.resizable(0,0)
    segundaVentana.geometry("400x400")
    segundaVentana.config(bg=COLOR_FONDO)

    miFrame1 = Frame(segundaVentana, bg=COLOR_FONDO)
    miFrame1.pack()

    BlancosLabel = Label(miFrame1, text="Candidatos", bg=COLOR_FONDO)
    BlancosLabel.grid(row=1, column=0, padx=10, pady=10)

    BlancosLabel = Label(miFrame1, text="Partido Politico", bg=COLOR_FONDO)
    BlancosLabel.grid(row=1, column=1, padx=10, pady=10)

    impugnadosLabel = Label(miFrame1, text="Votos", bg=COLOR_FONDO)
    impugnadosLabel.grid(row=1, column=2, padx=10, pady=10)

    validosLabel = Label(miFrame1, text="Porcentaje", bg=COLOR_FONDO)
    validosLabel.grid(row=1, column=3, padx=10, pady=10)
    

    for i in range(len(sistemaVotacion.listas)):

        textoLabel = sistemaVotacion.listas[i].candidatos[0].nombre
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=2 + i, column=0, padx=10, pady=10)

        textoLabel = sistemaVotacion.listas[i].parPolitico.nombre
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=2 + i, column=1, padx=10, pady=10)

        textoLabel = sistemaVotacion.listaCantidadVotos[sistemaVotacion.listas[i].numLista]
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=2 + i, column=2, padx=10, pady=10)

        textoLabel = str(sistemaVotacion.listaPorcentaje[sistemaVotacion.listas[i].numLista] )+ "%"
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=2 + i, column=3, padx=10, pady=10)
