##################
#Error
##################
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

def fx(x):
	return np.exp(-x)

def fx_1(x):
	return -np.exp(-x)

def derivar(metodo,x,h):

	if metodo==1:
		return (fx(x+h)-fx(x))/h
	if metodo==2:
		return (fx(x)-fx(x-h))/h
	if metodo==3:
		return (fx(x+(h/2))-fx(x-(h/2)))/h
	if metodo==4:
		t1=(4)*(fx(x+(h/4))-fx(x-(h/4)))/(h/2)
		t2=(fx(x+(h/2))-fx(x-(h/2)))/h	
		return (t1-t2)/3

def calcularError(real,numerica):
	return abs(real-numerica)	

x_1=np.linspace(-10,10,100)
h_0=np.logspace(-10,0,300)
x_0, h =np.meshgrid(x_1,h_0)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
e1,e2,e3,e4 = ax.plot_surface(x_0, np.log10(h), np.log10(calcularError(fx_1(x_0),derivar(1,x_0,h))),rstride=5,color="b"),ax.plot_surface(x_0, np.log10(h), np.log10(calcularError(fx_1(x_0),derivar(2,x_0,h))),rstride=5,color="r"),ax.plot_surface(x_0, np.log10(h), np.log10(calcularError(fx_1(x_0),derivar(3,x_0,h))),rstride=5,color="yellow"),ax.plot_surface(x_0, np.log10(h), np.log10(calcularError(fx_1(x_0),derivar(4,x_0,h))),rstride=5,color="purple")

plt.show()


plt.show()

