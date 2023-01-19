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