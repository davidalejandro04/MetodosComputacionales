import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

h=0.01
xi=0
xf=4
n=int((xf-xi)/h)
y=np.zeros(n)
x=np.zeros(n)


def f_prime(x,y):
	return -y

def LF():

	x[0]=xi
	y[0]=1.0
	x[1]=x[0]+h
	y[1]=y[0]+h*f_prime(x[0],y[0])
	for i in range(2,n):
		x[i]=x[i-2]+h
		y[i]=y[i-2]+2.0*h*f_prime(x[i-1],y[i-1])

	plt.plot(x,y,color='r')
	
def RK2():
	x[0]=xi
	y[0]=1.0
	for i in range(1,n):
		k1=h*f_prime(x[i-1],y[i-1])
		k2=h*f_prime(x[i-1]+h*0.5,y[i-1]+k1*0.5)
		x[i]=x[i-1]+h
		y[i]=y[i-1]+k2

	plt.plot(x,y,color='y')

def RK4():
	x[0]=xi
	y[0]=1.0
	for i in range(1,n):
		k1=h*f_prime(x[i-1],y[i-1])
		k2=h*f_prime(x[i-1]+h*0.5,y[i-1]+k1*0.5)
		k3=h*f_prime(x[i-1]+h*0.5,y[i-1]+k2*0.5)
		k4=h*f_prime(x[i-1]+h,y[i-1]+k3)
		slope=1.0/6.0*(k1+2.0*k2+2.0*k3+k4)
		x[i]=x[i-1]+h
		y[i]=y[i-1]+slope

	plt.plot(x,y,color='b')
	
LF()
RK2()
RK4()
plt.show()

#######################################################################
### 2 ecuaciones
#######################################################################

h=0.1
xi=0
xf=20
n=int((xf-xi)/h)
y_1=np.zeros(n)
y_2=np.zeros(n)
x=np.zeros(n)

a=1
b=0
g=0

def f_prime_1(xp,yp_1,yp_2):
	return yp_2

def f_prime_2(xp,yp_1,yp_2):
	return -a*yp_1-b*yp_2+g*np.cos(2*np.pi*xp)

def RK42():

	x[0]=xi
	y_1[0]=1.0
	y_2[0]=+0.01
	for i in range(1,n):
		k1=h*f_prime_1(x[i-1],y_1[i-1],y_2[i-1])
		l1=h*f_prime_2(x[i-1],y_1[i-1],y_2[i-1])
		k2=h*f_prime_1(x[i-1]+h*0.5,y_1[i-1]+k1*0.5,y_2[i-1]+l1*0.5)
		l2=h*f_prime_2(x[i-1]+h*0.5,y_1[i-1]+k1*0.5,y_2[i-1]+l1*0.5)
		k3=h*f_prime_1(x[i-1]+h*0.5,y_1[i-1]+k2*0.5,y_2[i-1]+l2*0.5)
		l3=h*f_prime_2(x[i-1]+h*0.5,y_1[i-1]+k2*0.5,y_2[i-1]+l2*0.5)
		k4=h*f_prime_1(x[i-1]+h*0.5,y_1[i-1]+k3,y_2[i-1]+l3)
		l4=h*f_prime_2(x[i-1]+h*0.5,y_1[i-1]+k3,y_2[i-1]+l3)

		slope_1=1.0/6.0*(k1+2.0*k2+2.0*k3+k4)
		slope_2=1.0/6.0*(l1+2.0*l2+2.0*l3+l4)
		x[i]=x[i-1]+h
		y_1[i]=y_1[i-1]+slope_1
		y_2[i]=y_2[i-1]+slope_2
	plt.plot(x,y_1)
	plt.plot(x,y_2)
	plt.show()




RK42()





