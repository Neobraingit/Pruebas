'''
 * Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
'''
def caracteres(str1, str2):
    for i in str1:
        if i not in str2:
            print (i)
        elif i not in str1:
            print (i)

caracteres('perro', 'gato')


