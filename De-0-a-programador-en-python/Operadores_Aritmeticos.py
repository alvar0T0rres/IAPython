# 1) Programa que solicite al usuario los datos para calcular el area de un Cuadrado
# 2) Programa que solicite al usuario los datos para calcular el area de un Triangulo
# 3) Programa que solicite al usuario los datos para calcular el area de un Circulo
# 4) Programa que solicite al usuario los datos para llevar Grados Fahrenheit a Grados Celcius
# 5) Sumar 4 Tramas de datos(String) que contengan el precio de un producto.
import math 

# *** Menu ***
menu = '''
[1] Area de un Cuadrado
[2] Area de un Triangulo
[3] Area de un Circulo
[4] Fahrenheit a Grados Celcius
[5] Sumar precios
'''
print(menu)
opcion = int(input('Ingrese la opcion deseada: '))

if(opcion == 1):
# *** 1 ***
# AREA DEL CUADRADO
# A = Lado ** 2
    ladoSquare = int(input('Ingrese el tamanio del lado del cuadrado: '))
    areaCuadrado = ladoSquare ** 2
    print(f'Area del cuadrado: {areaCuadrado}')

elif(opcion == 2):
# *** 2 ***
# AREA DEL TRIANGULO
# A = (Base * Altura) / 2
    baseTrian = int(input('Ingrese la base del Triangulo: '))
    alturaTrian = int(input('Ingrese la altura del Triangulo: '))
    areaTrian = (baseTrian * alturaTrian) /2
    print(f'Area del Triangulo {areaTrian}')

elif(opcion == 3):
# *** 3 ***
# AREA DEL CIRCULO
# A = PI * (Radio**2)
    radioCirc = int(input('Ingrese el radio del circulo: '))
    areaCirc = math.pi * (radioCirc ** 2)    
    #print(f'Area del circulo: {areaCirc}')
    print('Area del circulo: {0:.2f}'.format(areaCirc))

elif(opcion == 4):
# *** 4 ***
# FAHRENHEIT A CELCIUS
# Celcius = (Fahrenheit - 32.0) * 5.0 / 9.0
    fa = int(input('Ingrese los grados Fahrenheit que desea convertir: '))
    celciusCalc = (fa - 32.0) * 5.0/9.0
    print('Los grados Celcius son: {0:.2f}'.format(celciusCalc))

elif(opcion == 5):
# *** 5 ***
# SUMA DE PRECIOS
    precio1 = float(input('Ingrese el precio del primer producto: '))
    precio2 = float(input('Ingrese el precio del segundo producto: '))
    sumaProd = precio1 + precio2
    parte_decimal, parte_entera = math.modf(sumaProd)
    print(f'Suma: {sumaProd}')
    print(f'Parte Entera: {parte_entera}')
    print('Parte Decimal: {0:.3}'.format( parte_decimal))
