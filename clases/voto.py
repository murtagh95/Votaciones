class Voto():
    def __init__(self, lista, blanco = False, impugnado = False, valido = False):
        self.lista = lista
        self.blanco = blanco
        self.impugnado = impugnado
        self.valido = valido
    
    def __str__(self):
        return  "Voto a lista: {}, \n¿Voto blanco?: {}, \n¿Voto impugnado?: {}, \n¿Voto valido?: {},".format(
            self.lista,
            self.blanco,
            self.impugnado,
            self.valido,
            )

