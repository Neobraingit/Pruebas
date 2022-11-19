print (''' __   __  _______  __   __  _______  ______      ______   _______    _______  ______   _______  ______  
|  |_|  ||   _   ||  | |  ||       ||    _ |    |      | |       |  |       ||      | |   _   ||      | 
|       ||  |_|  ||  |_|  ||   _   ||   | ||    |  _    ||    ___|  |    ___||  _    ||  |_|  ||  _    |
|       ||       ||       ||  | |  ||   |_||_   | | |   ||   |___   |   |___ | | |   ||       || | |   |
|       ||       ||_     _||  |_|  ||    __  |  | |_|   ||    ___|  |    ___|| |_|   ||       || |_|   |
| ||_|| ||   _   |  |   |  |       ||   |  | |  |       ||   |___   |   |___ |       ||   _   ||       |
|_|   |_||__| |__|  |___|  |_______||___|  |_|  |______| |_______|  |_______||______| |__| |__||______| 
 by Marcos Carmona García\n''')

print ('Bienvenid@ a mi programa')
print('Necesito saber 2 cosas antes de comenzar: \nTu año de nacimiento\nTu nombre')
año = int(input('¿Qué año es en el que has nacido? '))
año_actual = 2022
print ('Bien¡¡ me encanta ese {} '.format(año))
nombre = input('Presentémonos, ¿cómo te llamas? ')
print (f'Encantado de conocerte, {nombre}')
print ('Basándome en tus datos, eres mayor de edad y tienes:',año_actual - año, 'años')