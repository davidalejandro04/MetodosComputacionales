import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy.linalg as linalg


a=np.array(pd.read_csv('DatosBancoMundial5.csv',skiprows=1,header=None))
a=a[:,4:]


Z=np.zeros(a.shape)

for i in range(0,Z.shape[0]):
	Z[i]=(a[i]-np.mean(a[i])) / (a[i].std())

fig,(ax1,ax2,ax3,ax4,ax5)=plt.subplots(5,1)
ax1.hist(Z[0],bins=25,color='red',label='Tax Rate')
ax1.set_title('Datos Normalizados Banco Mundial')

ax1.legend(loc=0)
ax2.hist(Z[1],bins=25,color='b',label='Cost of Bussiness Start')
ax2.legend(loc=0)
ax3.hist(Z[2],bins=25,color='y',label='Unemployement female')
ax3.legend(loc=0)
ax4.hist(Z[3],bins=25,color='g',label='Unemployement male')
ax4.legend(loc=0)
ax5.hist(Z[4],bins=25,color='purple',label='Ratio of female to male')
ax5.legend(loc=0)

plt.savefig('ExploracionDatos.pdf')
plt.close()


cov=np.zeros((5,5))

for i in range(0,5):
	for j in range(0,5):
		ti=Z[i]-np.mean(Z[i])
		tj=Z[j]-np.mean(Z[j])
		cov[i,j]=sum(ti*tj)/(Z.shape[1]-1)		
print("la matriz de covarianza es: ")

print(cov)




def eigencosos():
	#Obtengo valores y vectores propios
	eigenValores,eigenVectores=np.linalg.eig(cov)
	#Ordeno valores y vectores propios
	n = eigenValores.argsort()[::-1]   
	eigenValores = eigenValores[n]
	eigenVectores = eigenVectores[:,n]
	return eigenValores, eigenVectores


Valores,Vectores=eigencosos()
print(Valores)
print(Vectores)

pc1=[Valores[0],Vectores[:,0]]
pc2=[Valores[1],Vectores[:,1]]
print("La primera componente principal es: ")
print(pc1[1])
print(" con valor: %f"%pc1[0])
print("La segunda componente principal es: ")
print(pc2[1])
print(" con valor: %f"%pc2[0])

#Datos
nuevo=np.dot(Vectores.T,Z)
plt.scatter(nuevo[0,:],nuevo[1,:],label='Datos')
plt.xlabel('Primera componente principal')
plt.ylabel('Segunda componente principal')
plt.legend()
plt.title('Datos en plano principal')
plt.savefig('PCAdatos.pdf')
plt.close()

#Variables
nuevo2=np.dot(nuevo,Z.T)
plt.scatter(nuevo2[0,0],nuevo2[1,0],s=100,color='r',label='Tax Rate')
plt.scatter(nuevo2[0,1],nuevo2[1,1],s=100,color='b',label='Cost of Bussiness Start')
plt.scatter(nuevo2[0,2],nuevo2[1,2],s=100,color='y',label='Unemployement female')
plt.scatter(nuevo2[0,3],nuevo2[1,3],s=100,color='g',label='Unemployement male')
plt.scatter(nuevo2[0,4],nuevo2[1,4],s=100,color='purple',label='Ratio of female to male')
plt.xlabel('Primera componente principal')
plt.ylabel('Segunda componente principal')
plt.title('Variables en plano principal')
plt.legend()
plt.savefig('PCAvariables.pdf')
