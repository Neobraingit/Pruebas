frase = input('Escribe una frase o palabra: ')
frase = frase.lower()
vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in vocales:
    contador = 0
    for letra in frase:
        if letra == vocal:
            contador += 1
    print ('La vocal ' + vocal + ' aparece ' + str(contador)  + ' veces')
