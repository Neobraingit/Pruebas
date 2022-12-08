frase = input('Introduce una frase: ')
frase = frase.lower()
vocales = 'aeiou'
for vocal in vocales:
    contador = 0
    for i in frase:
        if i == vocal:
            contador +=1
    print ('La vocal', vocal, 'se repite', contador, 'veces.')