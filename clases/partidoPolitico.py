class PartidoPolitico():
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return "El partido politico se llama {}".format(self.nombre)
