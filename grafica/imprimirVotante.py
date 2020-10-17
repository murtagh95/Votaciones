from tkinter import *


def limpar(miFrame1, COLOR_FONDO):
    Label(miFrame1, text="\t\t", bg=COLOR_FONDO).grid(row=3, column=0, padx=10, pady=10)

    Label(miFrame1, text="\t\t", bg=COLOR_FONDO).grid(row=3, column=1, padx=10, pady=10)
 
    Label(miFrame1, text="\t", bg=COLOR_FONDO).grid(row=3, column=2, padx=10, pady=10)

    Label(miFrame1, text="\t", bg=COLOR_FONDO).grid(row=3, column=3, padx=10, pady=10)

    Label(miFrame1, text="\t\t\t\t", bg=COLOR_FONDO).grid(row=3, column=4, padx=10, pady=10)
    print("limpieza")

def imprimirVotante(sistemaVotacion, entry, miFrame1, COLOR_FONDO):
    votante = sistemaVotacion.buscarDNI(entry.get())
    limpar(miFrame1, COLOR_FONDO)

    if type(votante) != type(""):

        textoLabel = votante.nombre
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3, column=0, padx=10, pady=10)

        textoLabel = votante.apellido
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3, column=1, padx=10, pady=10)

        textoLabel = votante.edad
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3, column=2, padx=10, pady=10)

        textoLabel = votante.dni
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3, column=3, padx=10, pady=10)

        textoLabel = votante.direccion.calle + " Nº " + str(votante.direccion.num) + " , " + votante.direccion.barrio 
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3, column=4, padx=10, pady=10)
    else:
        Label(miFrame1, text=votante, bg=COLOR_FONDO, fg="red").grid(row=3, column=2, columnspan=2, padx=10, pady=10)
