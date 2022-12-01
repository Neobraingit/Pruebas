'''
Imprime por pantalla el texto: 'Introduce el primer número'
Crear la variable dato1 con el valor introducido en el paso anterior
Imprime por pantalla el texto: 'Introduce el segundo número'
Crear la variable dato2 con el valor antes introducido
Convertir la variable dato1 en una variable numérica denominada número1
Convertir la variable dato2 en una variable numérica denominada número2
Crear la variable suma con la suma de las dos anteriores
Convertir la variable suma en un string
Crear la variable resultado con la concatenación de 'La suma es' y 'strsuma'
Imprimir el valor de resultado
'''
print ('Introduce el primer número: ')
dato1 = int(input())
print ('Introduce el segundo número: ')
dato2 = int(input())
numero1 = dato1
numero2 = dato2
suma = numero1 + numero2
suma = str(suma)
resultado = 'La suma es ' + suma
print (resultado)