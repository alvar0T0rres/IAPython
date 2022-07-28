# Introducir dos numeros naturales por teclado. Imprimir los numeros naturales que hay entre ambos numeros empezando por el mas pequeno. 

num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese un numero: '))
aux = 0

if num1 > num2:
    aux = num2
    num2 = num1
    num1 = aux

while num1 <= num2:    
    print(num1)
    num1 += 1

