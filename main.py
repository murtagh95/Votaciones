from clases import *

PARTIDOS_POLITICOS = [
    PartidoPolitico("Juntos por el cambio"),
	PartidoPolitico("Frente de todos"),
	PartidoPolitico("Consenso Federal"),
	PartidoPolitico("Unite"),
    PartidoPolitico("Fit unidad"),
 	PartidoPolitico("Frente nos"),
]

# for partido in PARTIDOS_POLITICOS:
#     print(partido)

padron = Padron(25, "Escuela Villanueva", 15, Fecha(15, 5, 2019))
padron1 = Padron(45, "Escuela Mitre", 105, Fecha(15, 5, 2019))

votante = Votante("Nicolas", "Catalano", 38760722, 25, False, padron)

print(votante)
print("--------------------------")
albertoF = Candidato("Alberto", "Fernadez", 1165789, 99, False, padron1, "Abogado", "Presidente", True)

print(albertoF)
print("--------------------------")

lista1 = Lista(PARTIDOS_POLITICOS[0], 508, albertoF)
print(lista1)


