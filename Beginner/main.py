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

print(f"{row1}\n{row2}\n{row3}")