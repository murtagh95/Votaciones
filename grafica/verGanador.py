from tkinter import *


def verGanador(raiz, sistemaVotacion, COLOR_FONDO):
    ganador = sistemaVotacion.buscarGanador()
    
    # Creo una segunda ventana
    segundaVentana = Toplevel(raiz)
    segundaVentana.resizable(0,0)
    segundaVentana.geometry("500x200")
    segundaVentana.config(bg=COLOR_FONDO)

    miFrame1 = Frame(segundaVentana, bg=COLOR_FONDO)
    miFrame1.pack()

    if len(ganador) == 2:
        Label(miFrame1, text="El candidato ganador es:", bg=COLOR_FONDO).grid(row=1, column=0, columnspan=6, padx=10, pady=10)
    else:
        Label(miFrame1, text="Candidatos que iran a la segunda vuelta:", bg=COLOR_FONDO).grid(row=1, column=0, columnspan=6, padx=10, pady=10)

    
    Label(miFrame1, text="Nombre", bg=COLOR_FONDO).grid(row=2, column=0, padx=10, pady=10)
    Label(miFrame1, text="Apellido", bg=COLOR_FONDO).grid(row=2, column=1, padx=10, pady=10)
    Label(miFrame1, text="Puesto", bg=COLOR_FONDO).grid(row=2, column=2, padx=10, pady=10)
    Label(miFrame1, text="Partido Politico", bg=COLOR_FONDO).grid(row=2, column=3, padx=10, pady=10)
    Label(miFrame1, text="Lista", bg=COLOR_FONDO).grid(row=2, column=4, padx=10, pady=10)
    Label(miFrame1, text="Porcentaje votos", bg=COLOR_FONDO).grid(row=2, column=5, padx=10, pady=10)

    for i in range(0, (len(ganador) // 2)):

        textoLabel = ganador[i*2].candidatos[0].nombre
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3+i, column=0, padx=10, pady=10)

        textoLabel = ganador[i*2].candidatos[0].apellido
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3+i, column=1, padx=10, pady=10)

        textoLabel = ganador[i*2].candidatos[0].puesto
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3+i, column=2, padx=10, pady=10)

        textoLabel = ganador[i*2].parPolitico.nombre
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3+i, column=3, padx=10, pady=10)

        textoLabel = ganador[i*2].numLista
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3+i, column=4, padx=10, pady=10)

        textoLabel = str(ganador[1+(i*2)]) + "%"
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3+i, column=5, padx=10, pady=10)
        