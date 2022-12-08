'''
 * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
'''
def anagrama(string1, string2):
    if string1 == string2[::-1]:
        print ('Es un anagrama')
    else:
        print ('No es una anagrama')

anagrama('roma', 'amor')