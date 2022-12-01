'''
Crear una variable 'cadena' que contenga el texto: 'Esto es un texto de ejemplo'
Crear una variable 'longitud' que contenga la longitud de la variable 'cadena'
Crear una variable 'strlongitud' que contenga el valor de longitud, pero convertida a string
Crear una variable 'mayúsculas' que contenga la variable cadena en mayúsculas
Crear una variable 'resultado' que concatene 'mayúsculas' con el texto 'tiene longitud de' y 'strlongitud
'''

cadena = 'Esto es un texto de ejemplo'
longitud = len(cadena)
strlongitud = str(longitud)
mayusculas = cadena.upper()
resultado = mayusculas + ' tiene longitud de ' + strlongitud
print (resultado)