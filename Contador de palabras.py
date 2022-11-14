frase = input('Introduce una frase: ')
palabra = input('Introduce una palabra: ')
contador = 0

for i in frase:
    if palabra not in  frase:
        contador += 1
        palabra = input('Introduce una palabra: ')
    else:
        print ('Bien¡¡¡ l a palabra está en la frase')
        break
