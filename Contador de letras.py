frase = input('Introduce una texto: ')
frase = frase.lower()
letra = input('Introduce la letra a contar: ')
letra = letra.lower()
contador = 0
for i in frase:
    if i in letra:
        contador += 1
print (contador)




