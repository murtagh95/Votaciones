from random import choice

lista = [0, 1, 2, 3]
listaFinal = []
listaAlAzar = []

for i in range(4):
    num = choice(lista)
    listaAlAzar.append(num)
    lista.remove(num)

for i in range(4):
	if i == 0:
		listaFinal.extend([listaAlAzar[i]] * 45)
	elif i == 1:
	    listaFinal.extend([listaAlAzar[i]] * 35)
	else:
		listaFinal.extend([listaAlAzar[i]] * 10)

print("Lista final",listaFinal.count(0))
print("Lista final",listaFinal.count(1))
print("Lista final",listaFinal.count(2))
print("Lista final",listaFinal.count(3))