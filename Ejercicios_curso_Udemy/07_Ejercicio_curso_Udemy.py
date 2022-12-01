'''
Crear una variable mínimo, con el valor 200
Crea una variable máximo, con el valor 500
Recoge un valor del teclado y almacénalo en la variable dato
Convierte la variable dato en un número y almacénalo en la variable número
Si el número es menor que el valor de mínimo mostrar el texto 'Valor bajo'
Si el número es mayor que el valor de máximo, mostrar el texto 'valor alto'
Si el número está entre el mínimo y el máximo mostrar 'valor medio'
'''

minimo = 200
maximo = 500
dato = int(input('Introduce tu entero: '))
numero = dato
if numero < minimo:
    print ('Valor bajo')
elif numero > maximo:
    print ('Valor alto')
else:
    print ('Valor medio')