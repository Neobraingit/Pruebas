def contador_vocales(s):
    cont = 0
    hay = True

    for caracter in s:
        if caracter in 'aeiouAEIOU':
            cont = cont + 1

            print(caracter)

    print('Hay: ', cont, 'Vocales en: ', s)



