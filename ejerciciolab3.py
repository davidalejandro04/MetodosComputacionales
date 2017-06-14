import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon 
from scipy.stats import norm 



n=np.random.exponential(1,100)
n_1,n_2=expon.fit(n)
plt.hist(n,normed=True, bins=200,color='r',alpha=0.2)

x=np.linspace(0,15,1000)
y=expon.pdf(x,n_1,n_2)

plt.plot(x,y,'o-')
plt.plot(x,y,'k-')
plt.show()

nGrande=[]
for i in range(1,1000):
	nGrande.append(sum(np.random.exponential(1,1000)))

n_11,n_22=norm.fit(nGrande)
print(n_11,n_22)

x=np.linspace(0,2000,10000)
plt.plot(x, norm.pdf(x,n_11,n_22), 'k-')
plt.plot(x, norm.pdf(x,n_11,n_22),'o-')
plt.hist(nGrande,normed=True, bins=100,color='r',alpha=0.2)
plt.show()
