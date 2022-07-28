# Introducir tantas frases por teclado como deseemos y contarlas

respuesta = 'S'
cont = 0

while respuesta == 'S' or respuesta == 'SI':
    frase = input('Ingrese una frase: ')
    respuesta = input('Desea ingresar otra frase?: ').upper()
    cont += 1

print(f'El numero de frases introducidas fueron: {cont}')
