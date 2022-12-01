'''
Crear una variable números que contenga una lista con los números del 1 al 10
Mostrar el valor de la variable números
Recoger un input y alamacenarlo en dato
Canvertir dato en numérico y alamacenarlo en la variable número
Si el valor de número está en la lista, mostrar 'Si'
Si el valor no está en la lista, mostrar 'No'
'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (numeros)
dato = int(input('Introducir un entero:'))
numero = dato
if numero in numeros:
    print ('Si')
else:
    print ('No')