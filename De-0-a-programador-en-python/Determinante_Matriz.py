'''
*** Enunciado ***
Escriba, y ejecute un programa para calcular el determinante de una matriz 3x3 mediante la regla de Sarrus.

*** Salida ***
>>> DETERMINANTE DE LA MATRIZ: 
'''
import numpy as np

def solicitar_datos():
    matriz = np.zeros([3,3])
    charar = np.chararray((3,5), itemsize=10, unicode=True)    
    print(''.center(40, '-'))
    print('DETERMINANTE DE UNA MATRIZ'.center(40, ' '))
    print(''.center(40, '-'))
    print('MATRIZ'.center(40, ' '))
    print(''.center(40, '-'))
    
    for i in range(len(matriz)):        
        charar[i][0] = '|'
        for j in range(len(matriz[i])):
           charar[i][j+1] = f' a{i+1}{j+1}'            
        charar[i][-1] = ' |'        
            
    for i in charar:
        cad = ''.join(i)
        print(cad.center(40, ' '))
    print(''.center(40, '-'))
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = float(input(f'Ingrese el valor de a{i+1}{j+1}: '))
    
    print(''.center(40, '-'))
    print('MATRIZ'.center(40, ' '))
    print(''.center(40, '-'))

    for i in matriz:        
        cad1 = ' '.join(str(x) for x in i)
        cad2 = '|' + ' ' + cad1 + ' ' + '|'
        print(cad2.center(40, ' '))
    print(''.center(40, '-'))            

    return matriz            
    
def determinante_Sarrus(matriz):    
    a11 = matriz[0][0]
    a12 = matriz[0][1]
    a13 = matriz[0][2]
    a21 = matriz[1][0]
    a22 = matriz[1][1]
    a23 = matriz[1][2]
    a31 = matriz[2][0]
    a32 = matriz[2][1]
    a33 = matriz[2][2]

    determinante = a11*((a22*a33) - (a32*a23)) - a21*((a12*a33) - (a32*a13)) + a31*((a12*a23) - (a22*a13))
    
    return determinante

def main():
    matriz = solicitar_datos()    
    resultado = determinante_Sarrus(matriz)    
    print(f'>>>DETERMINANTE DE LA MATRIZ: {resultado}')
    print(''.center(40, '-'))            

main()
