'''
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
'''

numero = int(input('Escribe un número: '))
if numero & numero == 0:
    print ('Es primo')
else:
    print ('No es primo')