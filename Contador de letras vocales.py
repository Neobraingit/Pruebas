frase = input('Introduce una frase: ')
vocales = 'aeiouAEIOU'
contador = 0
for i in frase:
    if i in vocales:
        contador += 1
print ('Hay', contador, 'vocales')