#Condicionantes
#sintaxis de una prueba logica if
"""
if condition:
    do this
else:
    do this
"""

print("Bienvenidos a la montaña rusa.")
height = int( input("Cual es tu altura en cm: ") )

if height > 120:
    print("Tu puedes subir a la montaña")
else:
    print("Lo lamentamos pero no puedes subir a la montaña")

    """operadores de comparacion para condiciones logicas
    < menor que
    > mayor que
    >= mayor o igual
    <= menor o igual
    == exactamente igual
    != diferente de
    """
#operador modulo %
#este operador lo que hace es realizar una division y retornar el residuo de la division

7 % 2
# 7 se puede dividir en 2 + 2 + 2 + 1
# el output es 1 el residuo

#vamos a crear un programa que nos dice si un numero es par o impar
numero = int( input("Escribe el numero que quieras: ") )
if (numero % 2) == 0:
    print("tu numero es par")
else:
    print("tu numero es impar")

# Vamos a aplicar condiciones anidadas

print("Bienvenidos a la montaña rusa.")
height = int( input("Cual es tu altura en cm: ") )

if height >= 120:
    print("Tu puedes subir a la montaña")
    edad = int(input("Cuantos años tienes? "))
    if edad < 12:
        print("debes pagar 5 dolares")
    elif edad <= 18:
        print("debes pagar 7 dolares")
    else:
        print("debes pagar 12 dolares")
else:
    print("Lo lamentamos pero no puedes subir a la montaña")

#Vamos a hacer un indice de masa corporal 2.0 porque vamos a interpretar los resultados
    """la interpretacion del indice es la siguiente
    debajo de 18.5 esta bajo peso
    sobre 18.5 pero debajo de 25 es peso normal
    sobre 25 pero debajo de 30 sobrepeso
    sobre 30 pero debajo de 35 obesidad
    sobre 35 obesidad clinica
    """
Peso = int( input("Introduce tu peso en kilogramos:\n ") )
Altura = float ( input("Introduce tu estatura en metros:\n ") )
bmi = Peso / (Altura ** 2)
bmi_final = "{:.2f}".format(bmi)

if bmi < 18.5:
    print(f"Su indice de masa corporal es {bmi_final} esta en desnutricion")
elif bmi <= 25:
    print(f"Su indice de masa corporal es {bmi_final} es un peso normal")
elif bmi <= 30:
    print(f"Su indice de masa corporal es {bmi_final} esta en sobrepeso")
elif bmi <= 35:
    print(f"Su indice de masa corporal es {bmi_final} esta en obesidad")
else:
    print(f"Su indice de masa corporal es {bmi_final} tiene obesidad clinica")

#Vamos a hacer un programa que adivina si un programa es visiesto o no visiesto

    # """
    # si el año es divisible por 4 es bisiesto
    # excepto si este numero es divisible por 100
    # a menos que el año es ademas divisible por 400
    # """
year = int( input("Ingresa el año para saber si es bisiesto: ") )
year_4 = year % 4
year_100 = year % 100
year_400 = year % 400

if year_4 == 0:
    if year_100 == 0:
        if year_400 == 0:
            print("Es bisiesto")
        else:
            print("no es bisiesto")
    else:
        print("Es bisiesto")
else:
    print("no es bisiesto")

#Vamos a crear una condicion extra para el programa de la montaña rusa para ver si quieren una foto
print("Bienvenidos a la montaña rusa.")
height = int( input("Cual es tu altura en cm: ") )
#agregamos una variable que sea contador de la cuenta total de la montaña rusa
cuenta = 0

if height >= 120:
    print("Tu puedes subir a la montaña")
    edad = int(input("Cuantos años tienes? "))

    #esta primera condicion nos comprueba el rango de edad del usuario
    if edad < 12:
        #invocamos la variable de cuenta para agregar un valor en dependencia de la condicion
        cuenta = 5
        print(f"Ticket niños {cuenta} dolares")
    elif edad <= 18:
        cuenta = 7
        print(f"Ticket jovenes {cuenta} dolares")
    else:
        cuenta = 12
        print(f"Ticket adultos {cuenta} dolares")
    
    #creamos una variable en el scope de la primera condicion para que se ejecute luego de la primera condicion if
    quiere_foto = input("Quieres una foto? (Y or N): ")
    if quiere_foto == "Y":
        #si la condicion se cumple tomamos el ultimo valor de la variable en la condicion anterio y le sumamos 3
        cuenta += 3
    
    print(f"Tu cuenta final es {cuenta}")
else:
    print("Lo lamentamos pero no puedes subir a la montaña")

#Ejercicio para ordenar un pedido de pizza

bill = 0

print("Bienvenido a Pizza Delivery!")

size = input("que tamaño de pizza desea? S, M or L:\n ")
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Selecciona un opcion correcta")

add_pepperoni = input("Quieres pepperoni? Y or N:\n ")
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
    
extra_cheese = input("Quieres queso extra? Y or N:\n ")
if extra_cheese == "Y":
    bill += 1

print(f"tu cuenta es igual a ${bill}")

#logical operators para python
"""
    los operadores logicos son 
    AND lo que hace es evaluar condiciones, se tienen que cumplir todas
    OR lo que hace es alternar entre condiciones, se puede cumplir alguna
    NOT lo que hace es poner una restriccion, 
"""

a = 12
a > 15
#true
a > 10 and a < 13
#true
a > 15 and a < 13
#false
not a > 15
#true

#Añadiremos una condicion al programa de rollercoaster para dar tickets gratis a las personas
#si estan en la crisis de la mediana edad

print("Bienvenidos a la montaña rusa.")
height = int( input("Cual es tu altura en cm: ") )
#agregamos una variable que sea contador de la cuenta total de la montaña rusa
cuenta = 0

if height >= 120:
    print("Tu puedes subir a la montaña")
    edad = int(input("Cuantos años tienes? "))

    #esta primera condicion nos comprueba el rango de edad del usuario
    if edad < 12:
        #invocamos la variable de cuenta para agregar un valor en dependencia de la condicion
        cuenta = 5
        print(f"Ticket niños {cuenta} dolares")
    elif edad <= 18:
        cuenta = 7
        print(f"Ticket jovenes {cuenta} dolares")
    elif edad >= 45 and edad <= 55:
        print(f"Tienes una crisis de mediana edad por eso te regalamos una ticket")
    else:
        cuenta = 12
        print(f"Ticket adultos {cuenta} dolares")
    
    #creamos una variable en el scope de la primera condicion para que se ejecute luego de la primera condicion if
    quiere_foto = input("Quieres una foto? (Y or N): ")
    if quiere_foto == "Y":
        #si la condicion se cumple tomamos el ultimo valor de la variable en la condicion anterio y le sumamos 3
        cuenta += 3
    
    print(f"Tu cuenta final es {cuenta}")
else:
    print("Lo lamentamos pero no puedes subir a la montaña")

#Crearemos un programa que se llama lovescore de buzzfeed
"""las reglas son las siguientes:
    Vamos a tomar dos nombres de personas y en dependencia de la cantidad de veces que aparezcan en sus nombres
    las letras de la palabra TRUE LOVE vamos a sumarlas y vamos a crear un porcentaje para ello
    """

print("Bienvenido a la calculadora del amor: ")
primer_nombre = input("Ingresa tu nombre:\n ").lower()
segundo_nombre = input("ingresa el nombre del otro:\n ").lower()
nombre = primer_nombre + segundo_nombre
t = nombre.count("t")
r = nombre.count("r")
u = nombre.count("u")
e = nombre.count("e")
l = nombre.count("l")
o = nombre.count("o")
v = nombre.count("v")
e = nombre.count("e")

primer_digito = str(t + r + u + e)
segundo_digito = str(l + o + v + e)
score = int(primer_digito+segundo_digito)

if score <= 10 or score >= 90:
    print(f"Tu puntaje es {score}%, son tan compatibles como la coca y los mentos")
elif score >= 40 and score <= 50:
    print(f"Tu puntaje es {score}%, estarian bien juntos")
else:
    print(f"tu puntaje es {score}")

#Vamos a crear un juego de decisiones de tipo dungeon
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Bienvenido a la isla del tesoro.\nTu mision es encontrar el tesoro.")

camino = input("Estas en una encrucijada de caminos donde decides ir ¿a la derecha o izquierda? (D or I)\n ")

if camino == "I":
    rio = input("Caminando llegas a un rio, para pasarlo que vas a hacer ¿Nadar o Esperar? (N o E)\n ")
    if rio == "E":
        casa = input("El rio baja el caudal y llegas a un casa tres puertas con letras, cual eliges abrir ¿A, B o C?.\n ")
        if casa == "A":
            "Caes en lava y mueres calcinado hasta tu huesos, fin del juego."
        elif casa == "B":
            print("Encontraste el tesoro Felicidades")
        elif casa == "C":
            print("Eres comido por las bestias, fin del juego.")
        else:
            print("Game Over")
    else:
        print("Eres atacado por un lagarto, fin del juego.")
else:
    print("Caiste en un hoyo y moriste desangrado, se acabo el juego")