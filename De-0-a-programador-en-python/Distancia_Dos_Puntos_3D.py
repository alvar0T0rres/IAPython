'''
*** Enunciado ***
Determine la distancia entre dos puntos en el espacio: (x1,y1, z1) y (x2, y2, z2).
*** Salida ***
----------------------------------------
 DISTANCIA ENTRE 2 PUNTOS EN EL ESPACIO 
----------------------------------------
>>> Ingrese la coordenada x1: 10
>>> Ingrese la coordenada y1: 15
>>> Ingrese la coordenada z1: 20
----------------------------------------
>>> Ingrese la coordenada x2: 25
>>> Ingrese la coordenada y2: 30
>>> Ingrese la coordenada z2: 35
----------------------------------------
            DISTANCIA: 25.98            
----------------------------------------
'''

import math


print(''.center(50, '-'))
print('DISTANCIA ENTRE 2 PUNTOS EN EL ESPACIO'.center(50, ' '))
print(''.center(50, '-'))

X1 = float(input('>>> Ingrese la coordenada x1: '))
Y1 = float(input('>>> Ingrese la coordenada y2: '))
Z1 = float(input('>>> Ingrese la coordenada z2: '))
print(''.center(50, '-'))
X2 = float(input('>>> Ingrese la coordenada x2: '))
Y2 = float(input('>>> Ingrese la coordenada y2: '))
Z2 = float(input('>>> Ingrese la coordenada z2: '))

distancia = math.sqrt( ((X2-X1)**2) + ((Y2-Y1)**2) + ((Z2-Z1)**2) )

print(''.center(50, '-'))
print('DISTANCIA: {0:.4}'.format(distancia))
print(''.center(50, '-'))
