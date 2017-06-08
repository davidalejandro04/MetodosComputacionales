import sys

###Definir A y B. A par o impar. Divisores de A

A = input("Ingrese A: ")
B = input("Ingrese B: ")

print("A es igual a: %d y B es igual a: %d " %(A,B))

## Maximo comun divisor entre A y B

if(A%2==0):
	print("A es par")
else:
	print("A es impar")


div_A=[]
div_B=[]

for number in range(1,A+1):
	if(A%number==0):
		div_A.append(number)
	number+=1

for number in range(1,B+1):
	if(B%number==0):
		div_B.append(number)
	number+=1


print("Los divisores de A son: ")
for x in div_A:
    print(x)

print("Los divisores de B son: ")
for x in div_B:
    print(x)

print("El maximo comun divisor de A y B es : ")
maximo=1;
for x in div_A:
	for y in div_B:
		if x==y:
			maximo=x

print(maximo)



