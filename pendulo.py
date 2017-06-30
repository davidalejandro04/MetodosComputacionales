import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

h=0.1
xi=0
xf=20
yi=1.0
vi=0.0
l=1.0
g=9.8

n=int((xf-xi)/h)
y_1=np.zeros(n)
y_2=np.zeros(n)
x=np.zeros(n)

a=1
b=0
gamm=0

def f_prime_1(xp,yp_1,yp_2):
	return yp_2

def f_prime_2(xp,yp_1,yp_2):
	return -a*np.sin(yp_1)

def RK42():

	x[0]=xi
	y_1[0]=yi
	y_2[0]=vi
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
	return y_1,x

angulos,tiempos=RK42()
equises=0-l*np.sin(angulos)
yes=yi-l*np.cos(angulos)



fig, (ax, ax2) = plt.subplots(2,1)


line, = ax.plot([], [], 'o-', lw=2)
ax.set_xlim(-1.5*l,1.5*l)
ax.set_ylim(0,l)
ax.set_ylabel(r'$y$')
ax.set_xlabel(r'$x$')

ax.set_title('Posicion')
ax2.set_title(r'$\theta$'+' vs Tiempo')
ax2.plot(x,angulos)
ax2.set_ylabel(r'$\theta$')
ax2.set_xlabel(r'$Tiempo$')

def init():
    line.set_data([], [])
    return line


def animate(i):
    ax = [0, equises[i]]
    ay = [yi, yes[i]]

    line.set_data(ax, ay)
    return line

ani = animation.FuncAnimation(fig, animate, init_func=init)


plt.show()

