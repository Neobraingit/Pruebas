'''
Crear una variable 'conjunto' con los valores 1,2,3,4,5
Mostrar los valores de la variable conjunto
Añadir los números 6,7,8,9
Mostrar ahora el valor de la variable conjunto
Eliminar el número 9 de la variable
Mostrar el valor de la variable conjunto
Verificar que tipo de dato  es conjunto
'''

conjunto = {1,2,3,4,5}
print (conjunto)
conjunto.update({6,7,8,9})
print (conjunto)
conjunto.remove(9)
print (conjunto)
print (type(conjunto))