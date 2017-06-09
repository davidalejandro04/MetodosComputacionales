#######################################################################
###### Clases y Objetos
#######################################################################

import numpy as np

class Jugador:
	nombre = ""
	height = 0
	weight = 0
	#Must initialize on kg and m
	def asignarPesoEstatura(self, peso, estatura):	
		self.height=estatura
		self.weight=peso

	def peso(self,unidad)
		if unidad=="kg":		
			return self.weight
		else
			return self.weight*2.2

	def estatura(self)
		return self.height

	def function(self):
		print("This is  a message inside the class.", self.name)

jugador = Jugador()
jugador.asignarPesoEstatura()



##########Panda???#############


