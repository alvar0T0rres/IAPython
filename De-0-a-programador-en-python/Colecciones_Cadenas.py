# Author: Torres Velasco Alvaro Eduardo
# Manejo de colecciones y cadenas para mostrar la informacion con un formato en especifico.
# Resultados Esperado
##***************************************************************
##| Producto    |   Descripcion         | Cantidad  |   Precio  |
##***************************************************************
##| SmarthPhone |   Iphone 12 Pro Max   |     1     |   2000    |
##| SmarthPhone |   Iphone 11 Pro Max   |     1     |   1500    |
##| SmarthPhone |   Iphone 10 Pro Max   |     1     |   1200    |
##| SmarthPhone |   Iphone 09 Pro Max   |     1     |   1000    |
##***************************************************************
##|                                     |  Total    |   5700    |
##***************************************************************


# Declaracion de variables y colecciones
total = 0
list_Menu = ['Producto', 'Descripcion', 'Cantidad', 'Precio']
list_Producto1 = ['2000', '1', 'Iphone 12 Pro Max', 'Smarthphone']
list_Producto2 = ['1500', '1', 'Iphone 11 Pro Max', 'Smarthphone']
list_Producto3 = ['1200', '1', 'Iphone 10 Pro Max', 'Smarthphone']
list_Producto4 = ['1000', '1', 'Iphone 09 Pro Max', 'Smarthphone']
allProducts = [list_Producto1, list_Producto2, list_Producto3, list_Producto4]

# Se ordenan las listas
list_Producto1.reverse()
list_Producto2.reverse()
list_Producto3.reverse()
list_Producto4.reverse()

print(''.center(88, '*'))
print('|{:^20} |{:^20} |{:^20} |{:^20}|'.format(list_Menu[0],
                                               list_Menu[1],
                                               list_Menu[2],
                                               list_Menu[3]))
print(''.center(88, '*'))

# print('|{:^20} |{:^20} |{:^20} |{:^20}|'.format(list_Producto1[0],
#                                                list_Producto1[1],
#                                                list_Producto1[2],
#                                                list_Producto1[3]))
# print('|{:^20} |{:^20} |{:^20} |{:^20}|'.format(list_Producto2[0],
#                                                list_Producto2[1],
#                                                list_Producto2[2],
#                                                list_Producto2[3]))
# print('|{:^20} |{:^20} |{:^20} |{:^20}|'.format(list_Producto3[0],
#                                                list_Producto3[1],
#                                                list_Producto3[2],
#                                                list_Producto3[3]))
# print('|{:^20} |{:^20} |{:^20} |{:^20}|'.format(list_Producto4[0],
#                                                list_Producto4[1],
#                                                list_Producto4[2],
#                                                list_Producto4[3]))

# Se reducen todas las lineas anteriores de codigo con un ciclo FOR
for i in allProducts:    
    print('|{:^20} |{:^20} |{:^20} |{:^20}|'.format(i[0], i[1], i[2], i[3]))

print(''.center(88, '*'))
total = int(list_Producto1[3]) + int(list_Producto2[3]) + int(list_Producto3[3]) + int(list_Producto4[3])
print('|{:<21} {:>21} {:^20} |{:^20}|'.format(' ', ' ', 'Total', total))
print(''.center(88, '*'))