# Author: Torres Velasco Alvaro Eduardo
'''
*** Enunciad ***
Desarrollar un programa que genere el factorial de un número. 
Implementar y llamar a la funcion de forma recursiva. 
Mostrar el resultado de cada iteración en pantalla.

*** Salida ***
----------------------------------------
            NUMERO FACTORIAL            
----------------------------------------
>>> Introduce el numero a calcular: 10
----------------------------------------
>>> 0! = 1
>>> 1! = 1
>>> 2! = 2
>>> 3! = 6
>>> 4! = 24
>>> 5! = 120
>>> 6! = 720
>>> 7! = 5040
>>> 8! = 40320
>>> 9! = 362880
>>> 10! = 3628800
----------------------------------------
'''


def factorial(numero):
    if numero == 0:
        return 1
    elif numero == 1:
        return 1     
    else:
        return factorial(numero-1) * numero

print(''.center(40, '-'))
print('NUMERO FACTORIAL'.center(40, ' '))
print(''.center(40, '-'))
n = int(input('>>> Introduce el numero a calcular: '))
print(''.center(40, '-'))

for i in range(0, n+1):
    print(f'>>> {i}! = {factorial(i)}')
print(''.center(40, '-'))