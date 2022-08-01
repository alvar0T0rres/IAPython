# Imprimir 10 veces de una forma alternativa 'Hola' y 'Adios'

bandera = True
contador = 0

while contador < 10:
    if bandera:
        print('Hola')
        bandera = False
    else:
        print('Adios')
        bandera = True
    contador+=1        
        
