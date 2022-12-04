animales = {}
mientras = True
while mientras:
    clave = input('Introduce una clave: ')
    valor = input('Introduce un valor: ')
    animales[clave] = valor
    print (animales)
    continuar = print('¿Quieres introducir más datos? ') == 'Si'.lower()

