vocal = input('Introduce las letras a contar: ')
frase = input('Introduce una frase: ')
frase = frase.lower()
contador = 0
for i in frase:
    if i in vocal:
        contador += 1
print (contador)




