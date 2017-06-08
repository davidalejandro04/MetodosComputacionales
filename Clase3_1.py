
numbers = [    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,    743, 527]

for number in numbers:
	if (number%2 == 0):
		print ( number)
	
	if number==237:
		break


##############################
### Numpy arrays
##############################

height =[1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight =[81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
import numpy as np
np_height = np.array(height)
np_weight = np.array(weight)

##########################################
##Calcular bmi
#########################################

bmi=np_weight / np_height **2
print(bmi)
bmi >23
bmi[bmi>23]

###############################
#### Ejercicio 1
###############################

weight_kg=[81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
import numpy as np

np_weight_kg = np.array(weight_kg)
np_weight_lbs =np_weight_kg*2.2
print(np_weight_lbs)


###########a par impar, divisores de a maximo comun divisor

#############################################################################
## Funciones & recibir argumentos
##############################################################

nombre= raw_input("Cual es su nombre: ")

def my_function_with_args(username,greeting):
	print("Hello, %s, %s, the following are benefits of using functions" % (username,greeting))

my_function_with_args(nombre,"greetings")


#####################################################################
##########Ejercicio 2
#####################################################################

def list_benefits():
	return ["More organized code ","More readable code ","Easier code reuse ","Allowing programmers to share and connect code together "]

def build_sentence(benefit):
	return benefit+"is a benefit of functions!"

def name_the_benefits_of_functions():
	list_of_benefits = list_benefits()
	for benefit in list_of_benefits:
		print(build_sentence(benefit))

name_the_benefits_of_functions()


#######################################################################
######### FIN
######################################################################









