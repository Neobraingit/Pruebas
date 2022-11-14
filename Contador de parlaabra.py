frase = input('Introduce una frase: ')
letra = input ('Introduce la letra que quieras contar: ')
contador = 0
for i in frase:
    if i in letra:
        contador += 1
    re