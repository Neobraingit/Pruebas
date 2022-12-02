numero1 = int(input('Dame un número: '))
numero2 = int(input('Dame otro número'))
division = numero1 / numero2
if division == 1:
    try:
        print ('Esto es un error..')
    except:
        print ('El resultado es cero')
else:
    print ('Enhorabuena')
