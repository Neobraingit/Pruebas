'''
Crear un diccionario con los pares siguientes: 1 : one, 2 : two, 3 : three
Mostrar el diccionario por pantalla
Añadir un nuevo elemento al diccionario 4 : four
Mostrar el diccionario
Recoger un input y almacenarlo en dato
Utilizar dato como clave y recuperar su valor
'''

dic = {1 : 'one', 2 : 'two', 3 : 'three'}
print (dic)
dic[4] = 'four'
print (dic)
dato = input('Introduce un dato: ')
dic[dato] = dato