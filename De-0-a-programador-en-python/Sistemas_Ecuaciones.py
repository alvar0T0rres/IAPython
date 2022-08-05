'''
*** Enunciado ***
Realizar un programa que resuelva un sistema de ecuaciones utilizando el metodo de Cramer.

Sistemas de Ecuaciones
a11X1 + a12X2 = C1
a21X2 + a22X2 = C2

Metodo de Cramer
X1 = ( C1a22 - c2a12 ) / ( a11a22 - a12a21 )
X2 = ( C2a11 - c1a21 ) / ( a11a22 - a12a21 )

Ejemplo a solucionar

3X1 + 4X2 = 40
5X1 + 2X2 = 34
'''
import numpy as np

def metodo_cramer(matriz):    
    a11 = matriz[0][0]
    a12 = matriz[0][1]
    c1 = matriz[0][2] 
    a21 = matriz[1][0]
    a22 = matriz[1][1]
    c2 = matriz[1][2]    
    x1 = ( (c1*a22) - (c2*a12) ) / ( (a11*a22) - (a12*a21) )
    x2 = ( (c2*a11) - (c1*a21) ) / ( (a11*a22) - (a12*a21) )
    return x1, x2

def solicitar_datos():
    matriz = np.zeros([2,3])    
    
    print(''.center(40, '-'))
    for i in range(2):
        if i == 0: 
            print('PRIMER ECUACION'.center(40, ' ')) 
            print(''.center(40, '-'))
        else: 
            print(''.center(40, '-'))
            print('SEGUNDA ECUACION'.center(40, ' '))
            print(''.center(40, '-'))
        for j in range(2):
            matriz[i][j] = float(input(f'Ingrese el valor de X{j+1}: ')) 
        matriz[i][2] = float(input(f'Ingrese el valor de C{i+1}: '))       
    
    print(''.center(40, '-'))
    print('SISTEMA DE ECUACIONES'.center(40, ' '))
    print(''.center(40, '-'))
    for i in matriz:
        print(f'{i[0]}X1 + {i[1]}X2 = {i[2]}')
        
    return matriz
    
def main():
    matriz = solicitar_datos()
    resultado = metodo_cramer(matriz)
    print(''.center(40, '-'))
    print('RESULTADO'.center(40, ' '))
    print(''.center(40, '-'))
    print(f'X1 = {resultado[0]}'.center(40, ' '))
    print(f'X2 = {resultado[1]}'.center(40, ' '))
    print(''.center(40, '-'))

main()    
