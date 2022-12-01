'''
Crear una variable tupla con los siguientes índices Antonio, Pedro, María
Mostrar el valor tupla
Recoger un input y alamacenarlo en la variable dato
Si dato está en tupla, mostrar Si
Si dato no está en tupla, mostrar No
'''
tupla = ('Antonio', 'Pedro', 'María')
print (tupla)
dato = input('Introduce un dato: ')
if dato in tupla:
    print ('Si')
else:
    print ('No')