class Lista():
    def __init__(self, parPolitico, numLista, candidatos):
        self.parPolitico = parPolitico
        self.numLista = numLista
        self.candidatos = candidatos
    
    def mostrarCandidatos(self):
        consejales = ""
        for candidato in self.candidatos:
            consejales += "-{} {} .Candidato al puesto {}, titular {}\n".format(candidato.nombre, candidato.apellido, candidato.puesto, candidato.titular)
        
        return consejales

    def __str__(self):
        return  "Partido Politico: {}, Número Lista: {}, Candidato: \n{}".format(
            self.parPolitico.nombre,
            self.numLista,
            self.mostrarCandidatos(),
            )
