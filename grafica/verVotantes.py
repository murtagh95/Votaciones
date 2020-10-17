from grafica.plantillaMostrarPersona import crearPlantilla
from tkinter import *


def verVotantes(raiz, sistemaVotacion, COLOR_FONDO):
    contador = 0
    COLOR_RED = "#f26e50"
    
    # Creo una segunda ventana
    segundaVentana = Toplevel(raiz)
    segundaVentana.geometry("600x450")
    segundaVentana.resizable(0,0)
    segundaVentana.config(bg=COLOR_FONDO)

    # Creo barra de scroll y configuro
    scrollbar = Scrollbar(segundaVentana)
    c = Canvas(segundaVentana, yscrollcommand=scrollbar.set)
    scrollbar.config(command=c.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    # Creo el Frame y sigo configurando el scroll
    miFrame1 = Frame(segundaVentana, bg=COLOR_FONDO)
    miFrame1.pack()
    c.pack(side="left", fill="both", expand=True)
    c.create_window(0,0, window=miFrame1, anchor="nw")

    textoLabel= "Los votantes son {} y se mostraran a continuación".format(len(sistemaVotacion.votantes))
    Label(miFrame1, text=textoLabel, bg=COLOR_FONDO , fg=COLOR_RED).grid(row=1, column=0, columnspan=6, padx=10, pady=10)
    
    crearPlantilla(miFrame1, COLOR_FONDO)

    for votante in sistemaVotacion.votantes:

        textoLabel = votante.nombre
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3+contador, column=0, padx=10, pady=10)

        textoLabel = votante.apellido
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3+contador, column=1, padx=10, pady=10)

        textoLabel = votante.edad
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3+contador, column=2, padx=10, pady=10)

        textoLabel = votante.dni
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3+contador, column=3, padx=10, pady=10)

        textoLabel = votante.direccion.calle + " Nº " + str(votante.direccion.num) + " , " + votante.direccion.barrio 
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3+contador, column=4, padx=10, pady=10)

        contador += 1
    
    segundaVentana.update()
    c.config(scrollregion=c.bbox("all"))
