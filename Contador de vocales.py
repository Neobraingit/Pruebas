def contador_de_vocales():
    frase = input('Introduce una frase: ')
    contador = 0
    for letra in frase:
        if letra.lower() in ('aeiou'):
            contador += 1
    return contador

print (f' La frase tiene',contador_de_vocales(), 'vocales')






