frase = input('Introduce una frase: ')
frase = frase.lower()
letra = input('Introduce una letra: ')
letra = letra.lower()
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print (f'la letra {letra} aparece {contador} veces')