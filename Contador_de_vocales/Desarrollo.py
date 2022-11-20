

def contador ():
    frase = input('Introduce una frase: '.lower())
    letra = input('Introduce la letra a contar: '.lower())
    contador = 0
    for i in frase:
        if i in letra:
            contador += 1
    print (contador)
