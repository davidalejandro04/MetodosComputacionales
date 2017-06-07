
########################################################################
##Listas.
########################################################################
##Concatenar elementos de una lista
print("Ejercicio 1: Crear lista e imprimir")
mylist =[]
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])

for x in mylist:
	print(x)

#Acceder a elementos de una lista
print("Ejercicio 2: Acceder a elementos de una lista")
mylist =[1,2,3]
print(mylist[1])

#Ejercicio: Adicionar numeros y strings utiizando append

print("Ejercicio:")
numbers=[1,2,3]
strings=["numbers","hello","world"]
names=["John","eric","Jessica"]

second_name=names[1];

print(numbers)
print(strings)
print(second_name)


########################################################################
## Operadores Basicos
########################################################################

number= 1+2*3/4.0
print(number)

remainder=11%3
print(remainder)

squared=7**2
cubed=2**3

lotsofhellos="hello"*10
print(lotsofhellos)

even_numbers=[2,4,6,8]
odd_numbers=[1,3,5,7]
all_numbers= odd_numbers+even_numbers

print([1,2,3]*3)

############################################
###Ejercicio final##########################
############################################

x = object()
y = object()

x_list = [x] *10
y_list = [y] *10
big_list = x_list+y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")


##########################################################################
#########String formatting
########################################################################
#%s - String (or any object with a string representation, like numbers)
#%d - Integers
#%f - Floating point numbers
#%.<number of digits>f - Floating point numbers with a fixed amount of #digits to the right of the dot.
#%x/%X - Integers in hex representation (lowercase/uppercase)







