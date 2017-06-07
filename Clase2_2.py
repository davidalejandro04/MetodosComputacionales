#################################
######### Diccionarios
#################################

phonebook={}
phonebook["John"]=1235474
phonebook["Jack"]=5465423
phonebook["Jill"]=4654645
print(phonebook)

################################

phonebook={"John":1235474,"Jack":5465423,"Jill":4654645}
print (phonebook)
###########################################################
#### a %s se asocia el primer string, y a %d se asocia el numero
################################################################
phonebook={"John":1235474,"Jack":5465423,"Jill":4654645}
for name, number in phonebook.items():
	print("Phone number of %s is %d" % (name, number))
	print("The phone number is %d of %s " % (number, name))
########################################################
################Borrar elementos
#######################################################

phonebook ={ "John": 1235474,"Jack":5465423,"Jill":4654645}
del phonebook["John"]
print(phonebook)
phonebook["Juanito"]=1235474
print(phonebook)

############################################################
#########Ejercicios
#############################################################

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

phonebook["Jake"]=938273443
del phonebook["Jill"]
print(phonebook)


################################################################
####Condicionales
################################################################
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]
if number > 15:
    print("1")
if first_array:
    print("2")
if len(second_array) == 2:
    print("3")
if len(first_array) + len(second_array) == 5:
    print("4")
if first_array and first_array[0] == 1:
    print("5")
if not second_number:
    print("6")

#####################################################################
###############Loops################################################
#####################################################################

primes=[2,3,5,7]
for cosorandom in primes:
	print(cosorandom)

for x in range(5):
	print(x)

for x in range(3,6):
	print(x)

for x in range(3,8,2):
	print(x)
#####################################
#####Quejesto?
######################################

####################################
###While
####################################
count=0 
while count<5:
	print(count)
	count +=1
############################################


################################################
#########Break and continue
##################################################
count=0
while True:
#Condicion no incluida en while, sino en ruptura
	print(count)
	count +=1
	if count >=5:
		break
#Imprimir solo numeros impares
##Continue es como un skip para pasar al siguiente conteo del for
for x in range(10):
	if x%2==0:
		continue
	print(x)
###############################3
#########Else en loops 
###############################

count=0
while (count<5):
	print(count)
	count+=1
else:
	print("count value reached %d" %(count))

for i in range (1,10):
	if(i%5==0):
		break
	print(i)
else:
	print("this is not printed because for loop is terminated because of break but not due tofail in condition")


#################################################################
########Ejercicio
#################################################################

numbers = [    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,    743, 527]

for numero in numbers:
	if numero==237:
	print (numero)
	break

