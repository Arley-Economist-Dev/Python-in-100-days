#Data Types

#strings

#se usan slicers para traer la posicion del string
print("hello"[0])
#con el suma se concatena strings
print("hello" + "world")

# integer
print(123 + 2340)

#large integer
#con el underscore se reemplaza la coma de miles
123_344_988

#float
#son numeros decimales de variables continuas
3235.12

# boolean
True
False

# Funcion len
# esta funcion sirve para contar la extension de un string
num_char = len(input("what is your name: "))
# print("your name has " + num_char + "characters")

print( type(num_char) )

#Type convertion
# vamos a convertir a num_char en string
new_num_char = str(num_char)
print("your name has " + new_num_char + "characters")

a = 123
b = str(123)
c = float(a)
print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))

#Escribe un programa que tome un numero de dos digitos que lo separe y luego imprima la suma de ellos
str_num = str( input("Escribe un numero de dos digitos: ") )
print(str_num[0] + " + " + str_num[1] + " = " + str ( int(str_num[0]) + int(str_num[1]) ) )

#operaciones matematicas
1 + 5
7 - 4
3 * 2
6 / 3 #una division siempre retorna un float
2 ** 2 #los dos ** son para potenciar una cifra

#Jerarquia de operaciones PEMDAS
    # Parentesis ()
    # exponentes **
    # multiplicacion *
    # division /
    # adicion +
    # sustraccion -

#Ahora vamos a programar el indice de masa corporal de una persona
Peso = int( input("Introduce tu peso en kilogramos:\n ") )
Altura = float ( input("Introduce tu estatura en metros:\n ") )
print("Su indice de masa corporal es igual a: " +  str( int( Peso / (Altura ** 2) ) ) )

#como redondear un numero
print(round(8 / 3, 2))
print(round(3.2222, 1))

#float division este operador matematico te devuelve una division a integer
print( 8 // 3)

#este operador /= se usa para dividir por el resultado anterior al que se tenia

result = 4 / 2
result /= 2
print(result)
#output es 1.0

#este operador *= se usa para multiplicar por el resultado anterior al que se tenia

result = 4 / 2
result /= 2
print(result)
#output es 1.0

#este operador += se usa para agregar una cantidad a una cantidad previa
score = 0
score += 1
print(score)

#este operador += se usa para restar una cantidad a una cantidad previa
score = 1
score -= 1
print(score)

#Ahora vamos a usar f-strings
#esto se creo para agregar variables numericas dentro de strings
score = 0
altura = 1.8
ganador = True
#f-string
f"se añade una f antes de las comillas"
#se abren llaves para agregar una variable de otro tipo
print ( f"tu puntaje es de {score}, tu altura es {altura}, tu victoria es {ganador}" )

#Creando un programa que me dice cuantos dias de vida me quedan considerando que se supone que se viven 90 años
edad = int(input("Cual es tu edad actual:\n "))
years_restantes = 90 - edad
days_year = years_restantes * 365
week_year = years_restantes * 52
month_year = years_restantes * 12
print(f"te quedan {days_year} dias, {week_year} semanas y {month_year} meses")

#Este programa en cambio te dice cuanto tiempo has vivido
edad = int(input("Cual es tu edad actual:\n "))
days_year = edad * 365
week_year = edad * 52
month_year = edad * 12
print( f"has vivido {days_year} dias, {week_year} semanas y {month_year} meses" )


# #Vamos a crear una calculadora de propinas
"""
Vamos a asumir lo siguiente que la cuenta total es de 150
va a ser dividida por 5 personas, con un 12% de propina
cada persona debe pagar (total cuenta / cantidad de personas) multiplicado por el porcentaje
"""

total_cuenta = float( input("Bienvenidos a la calculadora de propinas.\n Ingresa el total de la cuenta: ") )
personas = int(input("Cuantas personas se dividiran la cuenta:\n "))
porcentaje = ( int( input ( "Ingresa el porcentaje de propina: " ) ) / 100 ) + 1
propina = ( total_cuenta / personas ) * porcentaje

#esta es una forma de resolverlo pero no se redondea con los valores en 0
# mensaje = f"La propina a pagar es de ${ round( ( total_cuenta / personas ) * porcentaje, 2 ) } por persona"

#se pueden usar diferentes formatos en python y se llaman como metodos para poder aplicarlo a valores numericos
propina_final = "{:.2f}".format(propina)

mensaje = f"La propina a pagar es de ${ propina_final } por persona"
print(mensaje)