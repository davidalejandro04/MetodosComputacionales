##################
#Derivadas
##################
import numpy as np
import matplotlib.pyplot as plt


def fx(x):

	return np.exp(-np.array(x)**2) / np.sqrt(2*np.pi)

#Derivar: Recibe como parametros las listas y, x; o: el orden de la derivada y m: el metodo (difCentral=1 o difAdelante=1)
def derivar(y,x,o,m=None):

	if m is None:
		m=0
	h         = x[1]-x[0]
	d_central,x_c = (y[2:]-y[0:-2])/(2*h), x[1:-1]
	d_forward,x_f = (y[1:]-y[0:-1])/(h), x[0:-1]
	d_second  = (y[2:]+y[0:-2]-(2*y[1:-1]))/(h*h)
	
	if o>2:
		while o>0:
			y,x=derivar(y,x,1,m)
			o-=1
		return y,x
	if o==1:
		if m==1:
			return d_forward,x_f
		else:
			return d_central,x_c 
	elif o==2:
		return d_second,x_c


x=np.linspace(-4,4,1000)
y=fx(x)
[dy,dx],[dyy,dxx],[dyyy,dxxx],[dyyyy,dxxxx]=derivar(fx(x),x,1,1),derivar(fx(x),x,2),derivar(fx(x),x,3),derivar(fx(x),x,4,1)

p,p1,p2,p3,p4 = plt.plot(x,y,label=r'$f(x)$'),plt.plot(dx,dy,label=r'$\frac{df}{dx}$'),plt.plot(dxx,dyy, label=r'$\frac{d^2 f}{d x^2}$'),plt.plot(dxxx,dyyy, label=r'$\frac{d^3 f}{d x^3}$'),plt.plot(dxxxx,dyyyy, label=r'$\frac{d^4 f}{d x^4}$')

plt.legend()

plt.show()




