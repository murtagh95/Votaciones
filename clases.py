class PartidoPolitico():
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return "El partido politico se llama {}".format(self.nombre)


class Direccion():
    def __init__(self, calle, num, barrio):
        self.calle = calle
        self.num = num
        self.barrio = barrio


class Persona():
    def __init__(self, nombre, apellido, dni, edad, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad
        self.direccion = direccion



class Fecha():
    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio

class Padron():
    def __init__(self, numMesa, lugar, fecha):
        self.numMesa = numMesa
        self.lugar = lugar
        self.fecha = fecha
    
    def __str__(self):
        return "Número mesa: {}, Lugar: {}, fecha: {}/{}/{}".format(
            self.numMesa,
            self.lugar,
            self.fecha.dia,
            self.fecha.mes,
            self.fecha.anio,
            )


class Votante(Persona):
    def __init__(self, nombre, apellido, dni, edad, direccion, voto, padronElectoral):
        super().__init__(nombre, apellido, dni, edad, direccion)
        self.voto = voto
        self.padronElectoral = padronElectoral

    def __str__(self):
        return "Nombre: {}, Apellido: {}, DNI: {}, Edad: {}, Dirección: {} {}/{}, Voto: {}, \n---Padron Electoral---\n {}".format(
            self.nombre,
            self.apellido,
            self.dni,
            self.edad,
            self.direccion.calle,
            self.direccion.num,
            self.direccion.barrio,
            self.voto,
            self.padronElectoral,
            )

class Candidato(Votante):
    def __init__(self, nombre, apellido, dni, edad, direccion, voto, padronElectoral, puesto, titular):
        super().__init__(nombre, apellido, dni, edad, direccion, voto, padronElectoral)
        self.puesto = puesto
        self.titular = titular

    def __str__(self):
        return  super().__str__() + "\nPuesto: {}, titular?: {}".format(
            self.puesto,
            self.titular,
            )
    


class Lista():
    def __init__(self, parPolitico, numLista, candidatos):
        self.parPolitico = parPolitico
        self.numLista = numLista
        self.candidatos = candidatos

    def __str__(self):
        return  "Partido Politico: {}, Número Lista: {}, Candidato: \n{}".format(
            self.parPolitico.nombre,
            self.numLista,
            self.candidatos,
            )


class Voto():
    def __init__(self, lista, blanco, impugnado, valido):
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

class SistemaVotacion():
    def __init__(self, listas, votantes, fecha, votos):
        self.listas = listas
        self.votantes = votantes
        self.fecha = fecha
        self.votos = votos

    def controlVotaciones(self):
        votosBlancos = 0
        votosImpugnados = 0
        votosValidos = 0
        for voto in self.votos:
            if voto.blanco:
                votosBlancos += 1
            elif voto.impugnado:
                votosImpugnados += 1
            else:
                votosValidos += 1
        return [votosBlancos, votosImpugnados, votosValidos]
    
    def porcentajeCandidato(self):
        listaPorcentaje = [0,0,0,0]
        
        for voto in self.votos:
            if voto.valido:
                if voto.lista.numLista == self.listas[0].numLista:
                    listaPorcentaje[0] += 1
                elif voto.lista.numLista == self.listas[1].numLista:
                    listaPorcentaje[1] += 1
                elif voto.lista.numLista == self.listas[2].numLista:
                    listaPorcentaje[2] += 1
                else:
                    listaPorcentaje[3] += 1
        
        for i in range(len(listaPorcentaje)):
            listaPorcentaje[i] = ((listaPorcentaje[i] * 100) / len(self.votos))


        return listaPorcentaje
        
    def buscarGanador(self, lista):
        pass





