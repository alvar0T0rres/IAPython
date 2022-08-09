# Author: Torres Velasco Alvaro Eduardo
'''
*** Enunciado ***
Diseña un programa que lea una matriz y muestre su transpuesta.

*** Salida ***
>>> MATRIZ ORIGINAL:
 
[1.0, 2.0, 3.0, 4.0]
[5.0, 6.0, 7.0, 8.0]
[9.0, 0.0, 1.0, 2.0]
 
>>> MATRIZ TRANSPUESTA:
 
[1.0, 5.0, 9.0]
[2.0, 6.0, 0.0]
[3.0, 7.0, 1.0]
[4.0, 8.0, 2.0]
'''

import numpy as np
print(''.center(40, '-'))
print('MATRIZ TRANSPUESTA'.center(40, ' '))
print(''.center(40, '-'))
filas = int(input('Ingrese el numero de filas: '))
columnas = int(input('Ingrese el numero de columnas: '))

matriz = np.zeros([filas, columnas])
matriz_t = np.zeros([columnas, filas])

print(''.center(40, '-'))
print('Ingrese los datos de la matriz: '.center(40, ' '))
for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = float(input(f'M({i}, {j}): '))

for i in range(columnas):
    for j in range(filas):
        matriz_t[i][j] = matriz[j][i] 

print(''.center(40, '-'))
print('>>> MATRIZ ORIGINAL: \n')
for i in matriz: print(i)
print(''.center(40, '-'))
print('>>> MATRIZ TRANSPUESTA: \n')
for i in matriz_t: print(i)
print(''.center(40, '-'))




