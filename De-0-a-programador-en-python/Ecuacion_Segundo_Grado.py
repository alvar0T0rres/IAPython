'''
*** Enunciado ***
Crear un Algoritmo que permita hallar la solución a una ecuación de segundo grado, de la forma:
                            ax^2 + bc + c = 0
Los datos del problema son los coeficientes a, b y c. Se desea calcular los valores de x que hacen cierta la ecuación.

*** Consideraciones ***
Este programa debe considerar la división por cero que tiene lugar cuando a vale 0 haciendo entonces al denominador,2a, nulo. 
Cuando a vale 0 la ecuación no es de segundo grado, sino de primer grado.
- Otra consideración que debemos tomar en cuenta es que el discriminante (b2- 4ac) no debe ser negativo, 
de ser negativo la ecuación no tiene soluciones reales.
Se deben tomar en cuenta los siguientes escenarios:
1) Si a es DIFERENTE de 0 (a != 0) la ecuación tiene solución.
Si b es DIFERENTE de 0 (b! = 0) la ecuación no tiene solución.
Se b es IGUAL a 0 (b == 0) se produce la división por cero, y la ecuación tiene infinitas soluciones.

*** Salida ***
-------------------------------------------------------
      ECUACION DE SEGUNDO GRADO: ax^2 + bx + c = 0      
-------------------------------------------------------
>>> Valor de a: 2
>>> Valor de b: 7
>>> Valor de c: 2
-------------------------------------------------------
>>> SOLUCIONES: x1 = -0.31 y x2 = -3.19
-------------------------------------------------------
'''
import math

print(''.center(60, '-'))
print('ECUACION DE SEGUNDO GRADO: ax^2 + bx + c = 0'.center(60, ' '))
print(''.center(60, '-'))

A = float(input('>>> Valor de a: '))
B = float(input('>>> Valor de b: '))
C = float(input('>>> Valor de c: '))
print(''.center(60, '-'))       
resultado = 0
solucion1 = 0
solucion2 = 0

if A == 0:    
    if B == 0:
        if C == 0:
            print('La ecuacion tiene infinitas soluciones'.center(60, ' '))
        else:
            print('La ecuacion no tiene solucion'.center(60, ' ')) 
    else:        
        resultado = -(C)/B         
        print(f'ECUACION: {A}x^2 + {B}x + {C} = 0'.center(60, ' '))
        print(''.center(60, '-'))
        print('>>> SOLUCION: x = {:.4}'.format(resultado))        
else:
    discriminante = (B**2) - 4*(A*C)
    if discriminante < 0:
        print('No existen soluciones reales'.center(60, ' '))
    else:
        solucion1 = (-B + math.sqrt(discriminante)) / (2*A)
        solucion2 = (-B - math.sqrt(discriminante)) / (2*A)
        print(f'ECUACION: {A}x^2 + {B}x + {C} = 0'.center(60, ' '))
        print(''.center(60, '-'))
        print('>>> SOLUCION: x1 = {:.3}  y  x2 = {:.3}'.format(solucion1, solucion2))        
print(''.center(60, '-'))
   