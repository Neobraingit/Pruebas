frase = input('Escribe una frase: ')
frase = frase.lower()
vocales = 'aeiou'
contador = 0
for i in frase:
    if i in vocales:
        contador += 1
print (contador)