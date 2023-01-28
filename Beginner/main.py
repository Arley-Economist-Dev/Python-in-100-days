#Password Generator

#dependencias
import random

#data
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Inicio
print("Bienvenido al generador de contraseñas!")
length = int ( input("Cuantas Letras te gustaria tener en la contraseña: \n") )
symbols = int ( input("Cuantos simbolos le gustaria tener?:\n ") )
numbers = int ( input("Cuantos numeros le gustaria tener?:\n ") )

#variable que almacena resultado
resultado = ""

#ciclos para seleccionar valores aleatorios de cada lista de datos
for i in range(1, length + 1):
    resultado += random.choice(letras)

for i in range(1, symbols + 1):
    resultado += random.choice(simbolos)

for i in range(1, numbers + 1):
    resultado += random.choice(numeros)

#usando el metodo shuffle para bajar una lista que recibe el resultado de los ciclos
l = list(resultado)
random.shuffle(l)
result = ''.join(l)

#imprime la contraseña
print(result)