# Matrices

import random

columns =int(input("Ingrese la cantidad de columnas del arreglo: "))
rows = int(input("Ingrese la cantidad de filas del arreglo: "))
even_numbers = ""
odd_numbers = 0
matrix = [[0 for _ in range(columns)] for _ in range(rows)]

for row in range(0,rows):
    for column in range(0,columns):
        matrix[row][column]= random.randint(100,200)

for row in range(0,rows):
    for column in range(0,columns):
        if matrix[row][column] % 2 == 0:
            even_numbers = even_numbers  + "El numero " + str(matrix[row][column]) + " es par y se encuentra en la posicion: " + str(row)+","+str(column) + "\n"
        else:
            odd_numbers = odd_numbers  + 1
print(matrix)
print(even_numbers)
print("La cantidad de numeros impares en la matriz es: ",odd_numbers)
