from grafica.plantillaMostrarPersona import crearPlantilla
from tkinter import *

   
def verNoVotantes(raiz, sistemaVotacion, COLOR_FONDO):
    reveldes = sistemaVotacion.buscarNoVotantes()
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
    # Creo el frame y sigo configurando el scroll
    miFrame1 = Frame(segundaVentana, bg=COLOR_FONDO)
    miFrame1.pack()
    c.pack(side="left", fill="both", expand=True)
    c.create_window(0,0, window=miFrame1, anchor="nw")

    textoLabel= "Las personas que no votaron son {}, se listaran a continuación".format(len(reveldes))
    Label(miFrame1, text=textoLabel, fg=COLOR_RED, bg=COLOR_FONDO).grid(row=1, column=0, columnspan=6, padx=10, pady=10)
    
    crearPlantilla(miFrame1, COLOR_FONDO)

    for revelde in reveldes:

        textoLabel = revelde.nombre
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3+contador, column=0, padx=10, pady=10)

        textoLabel = revelde.apellido
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3+contador, column=1, padx=10, pady=10)

        textoLabel = revelde.edad
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3+contador, column=2, padx=10, pady=10)

        textoLabel = revelde.dni
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3+contador, column=3, padx=10, pady=10)

        textoLabel = revelde.direccion.calle + " Nº " + str(revelde.direccion.num) + " , " + revelde.direccion.barrio 
        Label(miFrame1, text=textoLabel, bg=COLOR_FONDO).grid(row=3+contador, column=4, padx=10, pady=10)

        contador += 1
    
    segundaVentana.update()
    c.config(scrollregion=c.bbox("all"))
