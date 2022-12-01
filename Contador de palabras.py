frase = input('Introduce una frase: ')
frase = frase.lower()
palabra = input('Introduce una palabra: ')
palabra = palabra.lower()
contador = 0

for i in frase:
    if palabra not in  frase:
        contador += 1
        palabra = input('Introduce una palabra: ')
    else:
        print ('Bien¡¡¡ la palabra está en la frase')
        break
