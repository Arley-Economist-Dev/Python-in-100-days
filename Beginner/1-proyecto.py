# #Funcion print

# print("Day 1 - Python Print Function")
# print("The function is declared like this: ")
# print("print('what to print')")

# #aqui se explica un simbolo que separa en parrafos
# print("Hello world!\nHello World!")
# print("¿Hola como estas querido amigo?\nestoy practicando en python y esto es genial")

# #concatenamos con simbolo +
# print("Hello" + " " + "Arley")

# #Corregir el siguiente codigo
# print(Day 1 - String Manipulation")
# print('e.g. print("Hello " + "world")')
# print(("New Line can be created with a backlash and n.")
# #respuesta
# print("Day 1 - String Manipulation")
# print("e.g. print('Hello ' + 'world')")
# print("New Line can be created with a backlash and n.")

# #funcion input
# input("What is your name? ")
# print( "Hello " + input("What is your name? ") )

# #ejercicio para calcular la longitud de la cadena en el input
# print( len( input("What is your name? ") ) )

# # variables
# name = input("What is your name: ")
# print( name )

# name = input("What is your name? ")
# length = len(name)
# print(length)

# #otro ejercicio cambiando valores de variables
# a = input("a: ")
# b = input("b: ")
# c = a
# a = b
# b = c
# print("a: " + a)
# print("b: " + b)


"""
Aqui vamos a generar el programa generador de nombres de bandas, el algoritmo de creacion va a ser el siguiente
    1- crear un saludo para el programa
    2- preguntar por la ciudad donde la persona nacion
    3- preguntar el nombre de una mascota
    4- combinar el nombre de la ciudad con el de la mascota
"""

print("Hello Bienvenido al generador de nombre de bandas")
ciudad = input("Dime, ¿en que ciudad creciste?\n")
mascota = input("¿Cual es el nombre de tu mascota?\n")
print ( "El nombre de tu banda es "+ ciudad + " " + mascota)