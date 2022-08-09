# Author: Torres Velasco Alvaro Eduardo
'''
*** Enunciado ***
Un Freelancer desea saber cuánto puede cobrar por su trabajo semanal y mensualmente, para ello solo necesita 
establecer el precio de su trabajo por hora.
Se estiman 40 horas de trabajo a la semana.
Las Fórmulas para calcular el pago Semanal y Mensual son:
1) Pago_Semanal = (DolaresPorHora x 40)
2) Pago_Mensual = (DolaresPorHora x 160)

*** Salida ***
----------------------------------------
      CALCULADORA FREELANCER (USD)      
----------------------------------------
>>> Precio en dolares por Hora: 20
----------------------------------------
>>> PAGO SEMANAL: 800.00
>>> PAGO MENSUAL: 3200.00
----------------------------------------
'''

f_precioHora = 0
f_pagoSemanal = 0
f_pagoMensual = 0

print(''.center(50, '-'))
print('CALCULADORA FREELANCER (USD)'.center(50, ' '))
print(''.center(50, '-'))

f_precioHora = float(input('>>> Ingrese el precio en dolares por Hora: '))
f_pagoSemanal = f_precioHora * 40
f_pagoMensual = f_precioHora * 160

print(''.center(50, '-'))
print(f'>>> PAGO SEMANAL: {f_pagoSemanal}')
print(f'>>> PAGO MENSUAL: {f_pagoMensual}')
print(''.center(50, '-'))
