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