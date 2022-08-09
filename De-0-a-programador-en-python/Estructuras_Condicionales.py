# Author: Torres Velasco Alvaro Eduardo
# Introducir un numero por teclado y que se muestre un mensaje indicando si es multiplo de 3.

numero = int(input('Ingrese un numero: '))

if numero % 3 == 0:
    print('El numero es multiplo de 3')
else:
    print('El numero no es multiplo de 3')
