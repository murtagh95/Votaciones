from tkinter import *

def controlVotos(raiz, sistemaVotacion):
    
    # Creo una segunda ventana
    segundaVentana = Toplevel(raiz)
    segundaVentana.resizable(0,0)
    segundaVentana.geometry("250x150")
    segundaVentana.config(bg="#8eedd2")

    miFrame1 = Frame(segundaVentana, bg="#8eedd2")
    miFrame1.pack()

    # -----------MUESTRO LOS VOTOS EN BLANCO---------------------
    BlancosLabel = Label(miFrame1, text="Blancos", bg="#8eedd2")
    BlancosLabel.grid(row=1, column=0, padx=10, pady=10)

    textoLabel = sistemaVotacion.estadoDeVotos["Blancos"]
    BlancosValorLabel = Label(miFrame1, text=textoLabel, bg="#8eedd2")
    BlancosValorLabel.grid(row=2, column=0, padx=10, pady=10)

    # -----------MUESTRO LOS VOTOS IMPUGNADOS---------------------
    impugnadosLabel = Label(miFrame1, text="Impugnados", bg="#8eedd2")
    impugnadosLabel.grid(row=1, column=1, padx=10, pady=10)
    
    textoLabel = sistemaVotacion.estadoDeVotos["Impugnados"]
    BlancosValorLabel = Label(miFrame1, text=textoLabel, bg="#8eedd2")
    BlancosValorLabel.grid(row=2, column=1, padx=10, pady=10)

    # -----------MUESTRO LOS VOTOS VALIDOS---------------------
    validosLabel = Label(miFrame1, text="Validos", bg="#8eedd2")
    validosLabel.grid(row=1, column=2, padx=10, pady=10)
    
    textoLabel = sistemaVotacion.estadoDeVotos["Validos"]
    BlancosValorLabel = Label(miFrame1, text=textoLabel, bg="#8eedd2")
    BlancosValorLabel.grid(row=2, column=2, padx=10, pady=10)



def votosCandidatos(raiz, sistemaVotacion):
    
    # Creo una segunda ventana
    segundaVentana = Toplevel(raiz)
    segundaVentana.resizable(0,0)
    segundaVentana.geometry("400x400")
    segundaVentana.config(bg="#8eedd2")

    miFrame1 = Frame(segundaVentana, bg="#8eedd2")
    miFrame1.pack()

    BlancosLabel = Label(miFrame1, text="Candidatos", bg="#8eedd2")
    BlancosLabel.grid(row=1, column=0, padx=10, pady=10)

    BlancosLabel = Label(miFrame1, text="Partido Politico", bg="#8eedd2")
    BlancosLabel.grid(row=1, column=1, padx=10, pady=10)

    impugnadosLabel = Label(miFrame1, text="Votos", bg="#8eedd2")
    impugnadosLabel.grid(row=1, column=2, padx=10, pady=10)

    validosLabel = Label(miFrame1, text="Porcentaje", bg="#8eedd2")
    validosLabel.grid(row=1, column=3, padx=10, pady=10)
    

    for i in range(len(sistemaVotacion.listas)):

        textoLabel = sistemaVotacion.listas[i].candidatos[0].nombre
        Label(miFrame1, text=textoLabel, bg="#8eedd2").grid(row=2 + i, column=0, padx=10, pady=10)

        textoLabel = sistemaVotacion.listas[i].parPolitico.nombre
        Label(miFrame1, text=textoLabel, bg="#8eedd2").grid(row=2 + i, column=1, padx=10, pady=10)

        textoLabel = sistemaVotacion.listaCantidadVotos[sistemaVotacion.listas[i].numLista]
        Label(miFrame1, text=textoLabel, bg="#8eedd2").grid(row=2 + i, column=2, padx=10, pady=10)

        textoLabel = str(sistemaVotacion.listaPorcentaje[sistemaVotacion.listas[i].numLista] )+ "%"
        Label(miFrame1, text=textoLabel, bg="#8eedd2").grid(row=2 + i, column=3, padx=10, pady=10)

        
def verGanador(raiz, sistemaVotacion):
    ganador = sistemaVotacion.buscarGanador()
    
    # Creo una segunda ventana
    segundaVentana = Toplevel(raiz)
    segundaVentana.resizable(0,0)
    segundaVentana.geometry("500x200")
    segundaVentana.config(bg="#8eedd2")

    miFrame1 = Frame(segundaVentana, bg="#8eedd2")
    miFrame1.pack()

    if len(ganador) == 2:
        Label(miFrame1, text="El candidato ganador es:", bg="#8eedd2").grid(row=1, column=0, columnspan=6, padx=10, pady=10)
    else:
        Label(miFrame1, text="Candidatos que iran a la segunda vuelta:", bg="#8eedd2").grid(row=1, column=0, columnspan=6, padx=10, pady=10)

    
    Label(miFrame1, text="Nombre", bg="#8eedd2").grid(row=2, column=0, padx=10, pady=10)
    Label(miFrame1, text="Apellido", bg="#8eedd2").grid(row=2, column=1, padx=10, pady=10)
    Label(miFrame1, text="Puesto", bg="#8eedd2").grid(row=2, column=2, padx=10, pady=10)
    Label(miFrame1, text="Partido Politico", bg="#8eedd2").grid(row=2, column=3, padx=10, pady=10)
    Label(miFrame1, text="Lista", bg="#8eedd2").grid(row=2, column=4, padx=10, pady=10)
    Label(miFrame1, text="Porcentaje votos", bg="#8eedd2").grid(row=2, column=5, padx=10, pady=10)

    for i in range(0, (len(ganador) // 2)):

        textoLabel = ganador[i*2].candidatos[0].nombre
        Label(miFrame1, text=textoLabel, bg="#8eedd2").grid(row=3+i, column=0, padx=10, pady=10)

        textoLabel = ganador[i*2].candidatos[0].apellido
        Label(miFrame1, text=textoLabel, bg="#8eedd2").grid(row=3+i, column=1, padx=10, pady=10)

        textoLabel = ganador[i*2].candidatos[0].puesto
        Label(miFrame1, text=textoLabel, bg="#8eedd2").grid(row=3+i, column=2, padx=10, pady=10)

        textoLabel = ganador[i*2].parPolitico.nombre
        Label(miFrame1, text=textoLabel, bg="#8eedd2").grid(row=3+i, column=3, padx=10, pady=10)

        textoLabel = ganador[i*2].numLista
        Label(miFrame1, text=textoLabel, bg="#8eedd2").grid(row=3+i, column=4, padx=10, pady=10)

        textoLabel = str(ganador[1+(i*2)]) + "%"
        Label(miFrame1, text=textoLabel, bg="#8eedd2").grid(row=3+i, column=5, padx=10, pady=10)
        

def verConsejales(raiz, sistemaVotacion):
    consejales = sistemaVotacion.calcularConsejales()
    contador = 0
    
    # Creo una segunda ventana
    segundaVentana = Toplevel(raiz)
    segundaVentana.resizable(0,0)
    segundaVentana.geometry("400x400")
    segundaVentana.config(bg="#8eedd2")

    miFrame1 = Frame(segundaVentana, bg="#8eedd2")
    miFrame1.pack()

    Label(miFrame1, text="Los consejales ganadores son:", bg="#8eedd2").grid(row=1, column=0, columnspan=6, padx=10, pady=10)
    
    Label(miFrame1, text="Nombre", bg="#8eedd2").grid(row=2, column=0, padx=10, pady=10)
    Label(miFrame1, text="Apellido", bg="#8eedd2").grid(row=2, column=1, padx=10, pady=10)
    Label(miFrame1, text="Puesto", bg="#8eedd2").grid(row=2, column=2, padx=10, pady=10)
    Label(miFrame1, text="Partido Politico", bg="#8eedd2").grid(row=2, column=3, padx=10, pady=10)
    Label(miFrame1, text="Lista", bg="#8eedd2").grid(row=2, column=4, padx=10, pady=10)

    for consejal in consejales:

        textoLabel = consejal["candidato"].nombre
        Label(miFrame1, text=textoLabel, bg="#8eedd2").grid(row=3+contador, column=0, padx=10, pady=10)

        textoLabel = consejal["candidato"].apellido
        Label(miFrame1, text=textoLabel, bg="#8eedd2").grid(row=3+contador, column=1, padx=10, pady=10)

        textoLabel = consejal["candidato"].puesto
        Label(miFrame1, text=textoLabel, bg="#8eedd2").grid(row=3+contador, column=2, padx=10, pady=10)

        textoLabel = consejal["lista"].parPolitico.nombre
        Label(miFrame1, text=textoLabel, bg="#8eedd2").grid(row=3+contador, column=3, padx=10, pady=10)

        textoLabel = consejal["lista"].numLista
        Label(miFrame1, text=textoLabel, bg="#8eedd2").grid(row=3+contador, column=4, padx=10, pady=10)

        contador += 1
        



