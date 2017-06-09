import numpy as np
import matplotlib.pyplot as plt

latitud= np.genfromtxt(fname="sismos.txt", delimiter="\t", skiprows=(1),usecols=(20))

longitud= np.genfromtxt(fname="sismos.txt", delimiter="\t", skiprows=(1),usecols=(21))

print(latitud)
print(longitud)

plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.grid(True)
plt.plot(longitud,latitud,marker='o', color='b', ls='')
plt.show()

