import numpy as np
import matplotlib.pyplot as plt

infile = open('pg1524.txt','r')

lineas = infile.readlines()
palabras=[]
numeros=[]
cantidades=[]


for num in range(1,len(lineas)):
	palabras.extend(lineas[num].split(" "))
	






def contarPalabras(numero):
	cantidad=0

	for palabra in palabras:
		if len(palabra)==numero:
			cantidad+=1
	cantidades.append(cantidad)
	if numero!=0:
		print("el numero de palabras de %d letras es: %d " % ( numero, cantidad))
	else:
		pass

	

i=0


while i<20:
	contarPalabras(i)
	i+=1
	numeros.append(i)

plt.xlabel('Numero')
plt.ylabel('Cantidad')
plt.plot(numeros,cantidades)
plt.show()

infile.close()


