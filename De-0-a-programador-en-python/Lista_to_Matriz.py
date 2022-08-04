'''
*** Enunciado ***
La función debe permitir transformar los elementos de una lista simple en elementos de una matriz agrupándolos 
en filas y columnas. La función debe devolver la nueva lista y guardarla en una variable llamada “matriz”.

*** Salida ***
lista = [
                'a','b','c','d','e',
                'f','g','h','i','j',
                'k','l','m','n','o',
                'p','q','r','s','t',
                'u','v','w','x','y',
              ]
matriz = crear_matriz (fila, columna, nueva_lista)
'''
import numpy as np

def crear_matriz(fila, columna, lista):
    matriz = np.chararray((fila, columna))
    contador = 0
    for i in range(fila):
        for j in range(columna):
            matriz[i][j] = lista[contador]
            contador += 1
    return matriz

lista = [
                'a','b','c','d','e',
                'f','g','h','i','j',
                'k','l','m','n','o',
                'p','q','r','s','t',
                'u','v','w','x','y',
              ]
fila = 4
columna = 4

print(crear_matriz(fila, columna, lista))
