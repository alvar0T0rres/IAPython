'''
*** Enunciado ***
Imprime en pantalla una tabla con los nombres de los estudiantes y su promedio de notas.

*** Salida ***
+--------------------+----------+
|       NOMBRE       | PROMEDIO |
+--------------------+----------+ 
|Taylor C.           |      9.51|
+--------------------+----------+
|John G.             |      8.96|
+--------------------+----------+
|Maria S.            |      9.22|
+--------------------+----------+
|Juan C.             |      9.99|
+--------------------+----------+
|Anna A.             |      8.99|
+--------------------+----------+
|Mike T.             |      9.50|
+--------------------+----------+
|Pedro F.            |      9.99|
+--------------------+----------+
|Julia F.            |      8.99|
+--------------------+----------+
|Delia F.            |      9.89|
+--------------------+----------+
|Julio A.            |      7.50|
+--------------------+----------+
'''

estudiantes = [
    {'nombre': 'Taylor C.'  , 'promedio': 9.51},
    {'nombre': 'John G.'    , 'promedio': 8.96},
    {'nombre': 'Maria S.'   , 'promedio': 9.22},
    {'nombre': 'Juan C.'    , 'promedio': 9.99},
    {'nombre': 'Anna A.'    , 'promedio': 8.99},
    {'nombre': 'Mike T.'    , 'promedio': 9.50},
    {'nombre': 'Pedro F.'   , 'promedio': 9.99},
    {'nombre': 'Julia F.'   , 'promedio': 8.99},
    {'nombre': 'Delia F.'   , 'promedio': 9.89},
    {'nombre': 'Julio A.'   , 'promedio': 7.50}
]

print('+',''.ljust(20, '-'), '+', ''.ljust(10, '-'), '+')
print('|{:^22}|{:^12}|'.format('NOMBRE', 'PROMEDIO'))
print('+',''.ljust(20, '-'), '+', ''.ljust(10, '-'), '+')

for i in estudiantes:
    print('|{:^22}|{:^12}|'.format(i['nombre'], i['promedio']))
    print('+',''.ljust(20, '-'), '+', ''.ljust(10, '-'), '+')
    