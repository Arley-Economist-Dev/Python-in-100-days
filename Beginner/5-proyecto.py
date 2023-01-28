#Seccion de ciclos

#Ciclo for

#sintaxis
#for item in list_of_item:
    #do something

fruits = ["apple", "peach", "pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

#Challenge de codigo 1 - Average of heights
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)

# student_heights = [156, 124, 165, 173, 189, 169, 146]

#se genera un contador al que se le ira sumando los valores de cada elemento de la lista
#esta es la forma de sumar con un for
heights = 0
for h in student_heights:
    heights += h

#se genera un contador en cero y se le va añadiendo 1 por cada iteraccion a la lista
#esto es el equivalente a len pero con ciclos for
count = 0
for h in student_heights:
    count += 1

print ( f"El promedio de altura es { round( heights/count, 2 ) }" )

#Challenge de codigo 2 - vamos a encontrar el maximo con un ciclo for

#esta lista almacena las puntuaciones de estudiantes
scores = [78,65,89,86,55,91,64,89]

#se define una variable que contiene nada
max_value = None
#por cada valor de las puntuaciones
for i in scores:
    if max_value is None or i > max_value: max_value = i
    # el numero mayor debe cumplir una de las dos condiciones
    # el valor maximo es None o el valor i es mayor que el maximo
    # entonces el valor maximo se asigna a la variable
    # esto se itera hasta que la variable tiene el valor maximo
    
print(f"La puntuacion mas alta entre los estudiantes es: {max_value}")

#Funcion range para los loops

for i in range(1,10):
    print(i)
#output: los numeros se imprimen de 1 a 9

for i in range(1,11):
    print(i)

#el tercer parametro de range te indica el numero de saltos que da el numero
#hasta llegar al numero limite
for i in range(1, 11, 3):
    print(i)

#este es el problema de la suma de gauss para los primeros 100 numeros
total = 0
for i in range(1,101):
    total += i

print(total)

#Challenge de codigo 3 - vamos a encontrar el maximo con un ciclo for
#vamos a sumar todos los numeros de 1 al 100 pero si son pares

#creamos un contador
count = 0
#para cada numero en el rango
for i in range(1,101):
    #si el numero es par entonces se me suma al contador
    if i % 2 == 0: count += i

print(f"La suma de todos los numeros pares de 1 a 100 es {count}")

#vamos a sumar todos los numeros de 1 al 100 pero si son pares

#creamos un contador
count = 0
#para cada numero en el rango
for i in range(1,101):
    #si el numero es par entonces se me suma al contador
    if i % 2 == 0: count += i

#otra solucion hubiese sido
count = 0
for i in range(2,101,2):
    count += i

print(f"La suma de todos los numeros pares de 1 a 100 es {count}")

#Vamos a crear un programa que resuelve el problema fizz buzz

#para cada numero de este rango
for i in range(1,101):
    # si el numero es divisible por 3 y 5 entonces fizzbuzz
    if ( ( i % 3 == 0 ) & ( i % 5 == 0 ) ):
        i = "FizzBuzz"
    # si es divisible por 3 fizz
    elif (i % 3 == 0):
        i = "Fizz"
    # si es divisible por 5 buzz
    elif (i % 5 == 0):
        i = "Buzz"
    #imprimeme toda la secuencia de numeros
    print(i)

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