import numpy as np
import matplotlib.pyplot as plt


def fx(x):
	return np.cos(x)



def integrar(b,a,N):
	
	h=(float(b)-float(a))/(float(N)-1)
	x=np.linspace(float(a),float(b),N)
	y=fx(x)	
	integral=sum(h*y)-(h/2)*y[0]-(h/2)*y[N-1]

	plt.ylabel('f(x)')
	plt.xlabel('x')
	
	plt.fill_between(x, 0, y)
	plt.plot(x,y)


	print ("la integral de %f a %f de sin(x) es: %f") %(a,b,integral)




	


fa=input("ingrese a: ")
fb=input("ingrese b: ")
fN=input("ingrese N: ")



integrar(fb,fa,fN)
plt.show()

