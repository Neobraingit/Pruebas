def contador_de_vocales():
    frase = input('Introduce una frase: ')
    frase = frase.lower()
    letra = input ('Introduce la letra a contar: ')
    contador= 0
    for i in frase:
        if i in letra:
         contador += 1
    print (contador)


contador_de_vocales()
