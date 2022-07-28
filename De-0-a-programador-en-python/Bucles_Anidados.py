# Simular un reloj digital con el uso de bucles anidados
import time

hora = int(input('Ingrese la hora actual: '))
minuto = int(input('Ingrese el minuto actual: '))
segundo = 0

while hora < 24:        
    while minuto < 60:                        
        while segundo < 60:
            print(f'{hora}:{minuto}:{segundo}')
            segundo += 1            
            time.sleep(1)
        segundo = 0    
        minuto += 1        
    minuto = 0
    hora += 1                        
    
