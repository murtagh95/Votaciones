from tkinter import *

COLOR_TITULO = "#03076b"

def crearPlantilla(miFrame1, COLOR_FONDO):
    Label(miFrame1, text="Nombre", bg=COLOR_FONDO, fg=COLOR_TITULO).grid(row=2, column=0, padx=10, pady=10)
    Label(miFrame1, text="Apellido", bg=COLOR_FONDO, fg=COLOR_TITULO).grid(row=2, column=1, padx=10, pady=10)
    Label(miFrame1, text="Edad", bg=COLOR_FONDO, fg=COLOR_TITULO).grid(row=2, column=2, padx=10, pady=10)
    Label(miFrame1, text="DNI", bg=COLOR_FONDO, fg=COLOR_TITULO).grid(row=2, column=3, padx=10, pady=10)
    Label(miFrame1, text="Dirección", bg=COLOR_FONDO, fg=COLOR_TITULO).grid(row=2, column=4, padx=10, pady=10)

