import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt

rateDo, dataDo  = scipy.io.wavfile.read('Do.wav')
rateSol,dataSol = scipy.io.wavfile.read('Sol.wav')
dataDo=dataDo[:10000]
dataSol=dataSol[:10000]
print(dataDo.shape)
plt.plot(dataDo)
plt.plot(dataSol)
plt.show()
print(rateDo)
print(rateSol)
timestep=1.0/rateDo
freq = np.fft.fftfreq(dataDo.size, d=timestep);


def dft(xp):
	x= np.asarray(xp, dtype=float)
	N=x.shape[0]
	ies=[]
	jes=[]	
	for n in range(0,N):
		i=0
		j=0
		for k in range(0,N):
			i+=x[k]*np.cos(2*np.pi*k*n/N)
			j+=1j*x[k]*np.sin(2*np.pi*k*n/N)
		ies.append(i)
		jes.append(j)
	ies,jes=np.asarray(ies),np.asarray(jes)	
	Fourier=ies+jes    	
	return Fourier

def dftD(xp):
	x= np.asarray(xp, dtype=float)
	N=x.shape[0]
	ies=[]
	jes=[]	
	for n in range(0,N):
		i=0
		j=0
		
		for k in range(0,N):
			i+=x[k]*np.cos(8*np.pi*k*n/N)
			j+=1j*x[k]*np.sin(8*np.pi*k*n/N)
		ies.append(i)
		jes.append(j)
	ies,jes=np.asarray(ies),np.asarray(jes)	
	Fourier=ies+jes 
	Fourier[abs(freq)>1000]=0	
	return Fourier


#Fou=np.fft.fft(dataDo)
Fou=dft(dataDo)
FouD=dftD(dataDo)
FouSol=dft(dataSol)




def eliminarFMax(arreglo):
	arreglonuevo=arreglo.copy()
	mxm,imax=0,0
	for i in range(0,len(dataDo)):
		if(abs(arreglonuevo[i])>abs(mxm)):
			mxm=arreglonuevo[i]
			imax=i	

	rango=60
	for i in range(imax-rango,imax+rango):
		arreglonuevo[i]=0

	for i in range(-imax-rango,-imax+rango):
		arreglonuevo[i]=0
	return arreglonuevo



def pasabajas(arregloP):
	x=arregloP.copy()
	mxm,imax=0,0
	x[abs(freq)>1000]=0
	return x



fig,(ax1,ax2,ax3,ax4,ax5)=plt.subplots(5,1)
ax1.plot(freq,abs(Fou),color='g')
ax1.set_xlim(0,8000)
ax2.plot(freq,abs(FouD),color='b')
ax3.plot(freq,abs(FouSol),color='b')
ax4.plot(freq,abs(eliminarFMax(Fou)),color='b')
ax4.set_xlim(0,8000)
ax5.plot(freq,abs(pasabajas(Fou)),color='r')
ax5.set_xlim(0,8000)
plt.show()

#inversa=np.fft.ifft(FouD)
inversa=np.asarray(inversa,dtype=np.int16)
scipy.io.wavfile.write('DoRec.wav',rateDo,inversa)

