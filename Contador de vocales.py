def contador_de_vocales(frase):

    contador = 0
    for letra in frase:
        if letra.lower() in ('aeiou'):
            contador += 1
    return contador

print ('En la frase hay ', contador_de_vocales('aaaaaaaaaa'), 'vocales')



