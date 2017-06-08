#############################################################################
## Funciones & recibir argumentos
#############################################################
##Importar un string como un raw input
nombre= raw_input("Cual es su nombre: ")

def my_function_with_args(username,greeting):
	print("Hello, %d, from My Function!, I wish you %s" % (username,greeting))

my_function_with_args(nombre,"Saludos")


