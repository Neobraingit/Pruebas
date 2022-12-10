frase = input('Introduce una palabra: ')
contador = 0

for i in frase:
    if palabra not in frase:
        contador += 1
print (contador)