def contador_letras ():
    frase = input('Introduce una frasae: ')
    letra = input('Introduce una letra a contar: ')
    contador = 0
    for i in frase:
        if i in letra:
            contador += 1
    print ('Hay', contador, letra)

contador_letras()
