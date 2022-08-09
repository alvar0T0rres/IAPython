# Author: Torres Velasco Alvaro Eduardo
'''
*** Enunciado ***
Diseñar un programa que sume dos matrices. Recuerda que solo es posible sumar matrices con la misma dimensión
'''
import numpy as np
def suma_matriz(matriz1, matriz2):
    try:
        for i in range(len(matriz1)):
            for j in range(len(matriz1[i])):
                matriz1[i][j] = matriz1[i][j] + matriz2[i][j]
        return np.array(matriz1)
    except IndexError:
        print('Matrices con diferente dimension')
        return 0
    except:
        print('La matriz solo debe contener valores numericos')
        return 0

m1 = [[1,2,3], [4,5,6], [7,8,9]]
m2 = [[1,2,3], [4,5,6], [7,8,9]]
m3 = suma_matriz(m1, m2)

print(m3)

