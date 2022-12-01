'''
Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 * - lo resuelvan automáticamente.
'''
import re
frase = input('Introduce una frase: ')
resultado = len(frase.split())
print (resultado)


