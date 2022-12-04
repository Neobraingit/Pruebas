frase = input('Introduce un frase: ')
frase = frase.lower()
vocales = 'aeiou'
for vocal in vocales:
    contador = 0
    for letra in frase:
        if letra == vocal:
            contador += 1
    print ('La letra', vocal, 'sale', contador, 'veces')