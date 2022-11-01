class Contador ():
    def contador ():
        frase = input('Introduce una frase: ')
        frase.lower()
        letra  = input ('Introduce una letra: ')
        count = 0
        for i in frase:
            if i in letra:
                count += 1
                print ('La letra aparece ',count, 'veces')

    contador()






