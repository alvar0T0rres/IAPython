# Author: Torres Velasco Alvaro Eduardo
'''
*** Enunciado ***
Se coloca un capital, a un interés que oscila entre 0 y 100, durante cierta cantidad de años y se desea saber en cuanto se 
habrá convertido ese capital en cierta cantidad de años, sabiendo que es acumulativo.

*** Salida ****
----------------------------------------
        INTERES COMPUESTO (USD)         
----------------------------------------
>>> Capital Inicial: 1000
>>> Porcentaje de interes: 30
>>> Tiempo en Años: 10
----------------------------------------
          CAPITAL TOTAL: 13785.85          
----------------------------------------
'''

def interes_comp(capital, interes, anio):
    capital_total = capital
    for i in range(0, anio):
        capital = (capital_total * interes) / 100 
        capital_total += capital
    return capital_total

print(''.center(50, '-'))
print('INTERES COMPUESTO (USD)'.center(60, ' '))
print(''.center(50, '-'))

capital_inicial = float(input('>>> Capital Inicial: '))
porcentaje      = float(input('>>> Porcentaje de interes: '))
tiempo          = int(input('>>> Tiempo en anios: '))
resultado = interes_comp(capital_inicial, porcentaje, tiempo)
print(''.center(50, '-'))
print('CAPITAL TOTAL: {:.7}'.format(resultado).center(50, ' '))
print(''.center(50, '-'))