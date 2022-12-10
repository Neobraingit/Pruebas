'''
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 * las letras de otra palabra inicial.
 * - No hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
'''
def anagram (string1, string2):
    if string1 == string2[::-1]:
        print ('Es un anagrama')
    else:
        print ('No es un anagrama')

anagram('amor', 'roma')
