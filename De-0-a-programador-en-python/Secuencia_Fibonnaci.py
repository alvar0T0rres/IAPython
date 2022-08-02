'''
***Enunciado***
Desarrollar un programa que genere la secuencia de Fibonacci. Se debe crear y llamar recursivamente a la función. 
Se debe calcular la suma recursiva de los dos números anteriores (número-2) y (número-1). 
Mostrar el resultado de cada iteración en pantalla.
***Salida***
---------------------------------------------
            SUCESION DE FIBONACCI            
---------------------------------------------
>>> Introduce el valor deL termino 'n': 10
---------------------------------------------
>>> F(00) = 00
>>> F(01) = 01
>>> F(02) = 01
>>> F(03) = 02
>>> F(04) = 03
>>> F(05) = 05
>>> F(06) = 08
>>> F(07) = 13
>>> F(08) = 21
>>> F(09) = 34
>>> F(10) = 55
---------------------------------------------
'''
        
def fibonacci(numero):
    if(numero == 0):
        return 0
    elif(numero == 1):
        return 1
    else:        
        return (fibonacci(numero - 2) + fibonacci(numero - 1))
 
print(''.center(50, '-')) 
print('SUCESION DE FIBONACCI'.center(50, ' ')) 
print(''.center(50, '-')) 
n = int(input(">>> Introduce el valor deL termino 'n': "))
print(''.center(50, '-')) 

for i in range(0, n+1):
    print(f'>>> F{i} = {fibonacci(i)}')

print(''.center(50, '-')) 
