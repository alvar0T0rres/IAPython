# Author: Torres Velasco Alvaro Eduardo
'''
*** Enunciado ***
Se tiene los puntos A y B en el cuadrante positivo del plano cartesiano, elabore el algoritmo que 
permita obtener la distancia entre A y B.
Un punto en el plano tiene dos coordenadas (X ,Y), entonces el punto A tendrá sus coordenadas (AX, AY) 
y el punto B de manera similar (BX, BY).

*** Salida ***
----------------------------------------
  DISTANCIA ENTRE 2 PUNTOS EN EL PLANO  
----------------------------------------
>>> Ingrese la coordenada Ax: 2
>>> Ingrese la coordenada Ay: 4
----------------------------------------
>>> Ingrese la coordenada Bx: 8
>>> Ingrese la coordenada By: 12
----------------------------------------
            DISTANCIA: 10.00            
----------------------------------------
'''
import math

print(''.center(50, '-'))
print('DISTANCIA ENTRE 2 PUNTOS EN EL PLANO'.center(50, ' '))
print(''.center(50, '-'))

SOLICITUD_AX = float(input('>>> Ingrese la coordenada Ax: '))
SOLICITUD_AY = float(input('>>> Ingrese la coordenada Ay: '))
print(''.center(50, '-'))
SOLICITUD_BX = float(input('>>> Ingrese la coordenada Bx: '))
SOLICITUD_BY = float(input('>>> Ingrese la coordenada By: '))

distancia = math.sqrt(((SOLICITUD_AX - SOLICITUD_BX)**2) + ((SOLICITUD_AY - SOLICITUD_BY)**2))

print(''.center(50, '-'))
print(f'DISTANCIA: {distancia}'.center(50, ' '))
print(''.center(50, '-'))
