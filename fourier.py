import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt

rateDo, dataDo  = scipy.io.wavfile.read('Do.wav')
rateSol,dataSol = scipy.io.wavfile.read('Sol.wav')
#dataDo=dataDo[int(len(dataDo)*0.5):(int(len(dataDo)*0.5)+10*44100),1]
dataSol=dataSol[:]
dataDo=dataDo[:]

print(dataDo.shape)
plt.plot(dataDo)
plt.plot(dataSol)
plt.show()
print(rateDo)
print(rateSol)
timestep=1.0/rateDo
freqSol = np.fft.fftfreq(dataSol.size, d=timestep)
freq = np.fft.fftfreq(dataDo.size, d=timestep)
freq2 = np.fft.fftfreq(dataDo.size, d=timestep*391/260)



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


Fou=np.fft.fft(dataDo)
#Fou=dft(dataDo)
#FouD=dftD(dataDo)
#FouSol=dft(dataSol)
FouSol=np.fft.fft(dataSol)



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


bajas=abs(pasabajas(Fou))
altas=abs(eliminarFMax(Fou))
inversa=np.fft.ifft(Fou)
inversa1=np.fft.ifft(bajas)
inversa2=np.fft.ifft(altas)



fig,(ax1,ax2,ax3,ax4,ax5)=plt.subplots(5,1)
ax1.plot(freq,abs(Fou),color='g')
ax1.set_xlim(0,8000)
ax2.plot(freqSol,abs(FouSol),color='b')
ax2.set_xlim(0,8000)
ax3.plot(freq2,abs(Fou),color='b')
ax3.set_xlim(0,8000)
ax4.plot(freq,bajas,color='b')
ax4.set_xlim(0,8000)
ax5.plot(freq,altas,color='r')
ax5.set_xlim(0,8000)
plt.show()

inversa1=np.asarray(inversa,dtype=np.int16)
scipy.io.wavfile.write('Do_sol.wav',rateDo*391/260,inversa1)



"""
inversa2=np.asarray(inversa2,dtype=np.int16)
inversa1=np.asarray(inversa1,dtype=np.int16)
scipy.io.wavfile.write('Do_pasabajos.wav',rateDo,inversa1)
scipy.io.wavfile.write('Do_pico.wav',rateDo,inversa2)
"""




