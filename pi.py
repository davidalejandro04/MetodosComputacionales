import numpy as np
import matplotlib.pyplot as plt


def fx(x):
	return  4*(np.sqrt(1-x**2))


def integrar(b,a,N):
	
	h=(float(b)-float(a))/(float(N)-1)
	x=np.linspace(float(a),float(b),N)
	y=fx(x)	
	integral=sum(h*y)-(h/2)*y[0]-(h/2)*y[N-1]

	plt.ylabel('f(x)')
	plt.xlabel('x')
	
	plt.fill_between(x, 0, y)
	plt.plot(x,y)

	print ("Pi es: %f") %(integral)




	


fa=0
fb=1
fN=10000



integrar(fb,fa,fN)
plt.show()
