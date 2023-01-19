#En esta seccion vamos a entender como generar aleatoriedad a los programas.

import random

"""
random es un modulo, los modulos son archivos de python que contienen elementos
    que pueden ser llevados desde el archivo de python hasta este proyecto

import my_module #my_module seria un archivo .py
print(my_module.pi) #pi es una variable que estan en my_module

asi funciona random
"""

random_integer = random.randint(1,10)
print(random_integer)

random_float = random.random()
print(random_float)

random_float_entre_rango = random.uniform(0,5)
print(random_float_entre_rango)

love_score = random.randint(1,100)
print(f"Tu compatibilidad con esta persona es {love_score}%")

# #Moneda virtual
print("Bienvenido al lanzamiento de moneda virtual.")
moneda = random.randint(0,1)
if moneda == 0:
    print(f"Cara")
else:
    print(f"Cruz")

#listas

#las listas son un vector que almacena elementos en un orden determinado
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", 
"Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina",
"Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
"Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California",
"Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
"South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#gracias a ese orden podemos llamar al primer estado en unirse a estados unidos
print(states_of_america[0])
print(states_of_america[2])
print(states_of_america[-1]) #ultimo de la lista

states_of_america[1] = "Pencilvania"
states_of_america.append("Angelalandia")

states_of_america.extend(["Arley Paredes", "Econometria"])

#crearemos un programa para elegir pagar la cuenta automaticamente
nombres = input("Bienvenido al selector aleatorio para pagar la cena.\n Ingresa el nombre de todos los participantes (separado por una coma): ")
lista_nombres = nombres.split(", ")
print(f"{random.choice(lista_nombres)} es quien pagara la cuenta hoy.")

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", 
"Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina",
"Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
"Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California",
"Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
"South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

conteo_estados = len(states_of_america)
print(conteo_estados)
#50
print(states_of_america[49])
#hawaii
print(states_of_america[50])
#list index out of range
print( states_of_america[conteo_estados] - 1 )

dirty_dozen = ["Strawberries","Spinach","Kale","Nectarines","Apples",
"Grapes","Peaches","Cherries","Pears","Tomatoes","Celery","Potatoes"]

fruit = ["Strawberries","Nectarines","Apples",
"Grapes","Peaches","Cherries","Pears"]
vegetables = ["Spinach","Kale","Tomatoes","Celery","Potatoes"]

# podemos contener dos listas en una sola haciendo un nested list
dirty_dozen = [fruit, vegetables]
print(dirty_dozen)

#los slicers en las nested lists el primero es usado para elegir el indice de la lista que lo compone y el segundo es para el elemento de la sub lista
print(dirty_dozen[1][1]) #kale
print(dirty_dozen[1][2])
print(dirty_dozen[1])
print(dirty_dozen[0])

#Reto de juego para encontrar un tesoro en alguna posicion del tablero
row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]

#se crea una nested list para esta cuadricula
map = [row1, row2, row3]
#con esto se imprime la cuadricula
print(f"{row1}\n{row2}\n{row3}")

#aqui pedimos el input necesario para el juego
position = input("Where do you want to put the treasure?\n(first digit is column second is row): ")

#estas variables almacenan en numero los dos digitos
columna = int ( position[0] ) #2
fila = int ( position[1] ) #3

#se resta uno al valor de fila para evadir el problema de indices
selected_row = map[fila - 1]
#se navega hasta la ultima lista anidada del conjunto y se busca su indice en funcion de la columna
#este elemento de esa coordenada es reemplazado por una X
selected_row[columna - 1] = "X"

#OTra solucion puede ser
map[fila - 1][columna - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")


#Proyecto piedra papel o tijeras
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

elementos = [rock, paper, scissors]
seleccion = elementos [ int( input("Bienvenido a Piedra, Papel o Tijeras, ¿Cual eliges?\n (0 piedra, 1 papel, 2 tijeras): ") ) ]
aleatoria = random.choice(elementos)

print(f"Tu seleccionaste: \n {seleccion}")
print(f"La computadora selecciono: \n {aleatoria}")

if aleatoria == rock and seleccion == scissors:
    print("Pierdes la piedra rompe a la tijera")
elif aleatoria == rock and seleccion == paper:
    print("Ganas porque el papel envuelve a la piedra")
elif aleatoria == paper and seleccion == rock:
    print("Pierdes porque el papel envuelve a la piedra")
elif aleatoria == paper and seleccion == scissors:
    print("Ganas porque la tijera corta el papel")
elif aleatoria == scissors and seleccion == rock:
    print("Ganas porque la piedra rompe a la tijera")
elif aleatoria == scissors and seleccion == paper:
    print("Pierdes porque el papel es cortado por la tijera")
else:
    print("Eligieron lo mismo por lo tanto es un empate.")