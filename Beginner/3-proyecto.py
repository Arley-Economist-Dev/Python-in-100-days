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