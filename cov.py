import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as linalg


lineas=np.genfromtxt('roomtemperature.csv',delimiter=',', skiprows=(1),usecols=(1,2,3,4))

dimensiones=4

cov=np.zeros((4,4))

for i in range(0,4):
	for j in range(0,4):
		ti=lineas[:,i]-np.mean(lineas[:,i])
		tj=lineas[:,j]-np.mean(lineas[:,j])
		cov[i,j]=sum(ti*tj)/143		
print("la matriz de covarianza es: ")
print(cov)
#Calculo e imprimo los autovalores
Valores,Vectores=np.linalg.eig(cov)

n = Valores.argsort()[::-1]   
Valores = Valores[n]
Vectores = Vectores[:,n]
print("Los autovalores son: ")
print(Valores)
print("Los autovectores son: ")
print(Vectores)

nuevo=np.dot(Vectores.T,lineas.T)
print(nuevo)
fig = plt.figure(figsize=(13,4))
ax = plt.axes()
plt.scatter(nuevo[0,:], nuevo[1,:])
x_line = np.linspace(0,300.0,1000)
ax.set_aspect(1.0)
plt.show()

