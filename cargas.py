import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.gridspec as gridspec


fin=5
resolucion=50
x=np.linspace(0,fin,resolucion)
y=np.linspace(0,fin,resolucion)
v=np.zeros((len(x),len(y)))



e=-1.602176*(10**-16)
k=8.987*(10**27)/e
q=e

class Carga:

	x,y=0,0
	def __init__(self,xi,yi):
		self.x=xi
		self.y=yi
	def posicion(self):
		return self.x,self.y

	def voltaje(self,x,y):

		v_nuevo=np.zeros((len(x),len(y)))
		for i in range(0,len(x)):
			for j in range(0,len(y)):
#				if (x[i]!=self.x) and y[j]!=self.y:
					R=np.sqrt(   ((x[i]-self.x)*(x[i]-self.x))   +   ((y[j]-self.y)*(y[j]-self.y))  )
					v_nuevo[i,j]=(k*q)/R

		return v_nuevo
		

					

disesqu=0

c1,c2,c3,c4=Carga(disesqu,disesqu),Carga(disesqu,fin-disesqu),Carga(fin-disesqu,disesqu),Carga(fin-disesqu,fin-disesqu)
v=v+c1.voltaje(x,y)+c2.voltaje(x,y)+c3.voltaje(x,y)+c4.voltaje(x,y)

x_0, y_0 =np.meshgrid(x,y)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
e1= ax.plot_surface(x_0,y_0,v)
plt.show()
plt.close()
plt.contour(x_0,y_0,v)
plt.show()

def derivar(y,x):

	h         = x[1]-x[0]
	d_central,x_c = (y[2:]-y[0:-2])/(2*h), x[1:-1]
	
	return (y[2:]-y[0:-2])/(2*h)



U,V=-(derivar(v,x)), -(derivar(v,y))
x_0,y_0=np.meshgrid(x,y)
print(len(U))

speed = np.sqrt(U*U + V*V)



strm=plt.streamplot(x_0[1:-1], y_0[1:-1], V, U, color=U, linewidth=2, cmap='autumn')
plt.colorbar(strm.lines)

plt.show()


