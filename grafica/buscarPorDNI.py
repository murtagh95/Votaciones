from grafica.imprimirVotante import imprimirVotante
from grafica.plantillaMostrarPersona import crearPlantilla
from tkinter import *

def buscarPorDNI(raiz, sistemaVotacion, COLOR_FONDO):
    
    # Creo una segunda ventana
    segundaVentana = Toplevel(raiz)
    segundaVentana.resizable(0,0)
    segundaVentana.geometry("750x200")
    segundaVentana.config(bg=COLOR_FONDO)

    miFrame1 = Frame(segundaVentana, bg=COLOR_FONDO)
    miFrame1.pack()

    dniLabel = Label(miFrame1, text="Ingresar DNI:", bg=COLOR_FONDO)
    dniLabel.grid(row=1, column=0, columnspan=2, sticky="e", padx=10, pady=10)
    dniTexto = Entry(miFrame1)
    dniTexto.grid(row=1, column=2, padx=10, pady=10)
    # Obtenemos la información de la caja de texto 
    button = Button(miFrame1, text="Buscar", command=lambda: imprimirVotante(sistemaVotacion, dniTexto, miFrame1, COLOR_FONDO))
    button.grid(row=1, column=3)
    
    crearPlantilla(miFrame1, COLOR_FONDO)
