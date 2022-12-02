eco = input('Escribe cualquier cosa: ')
eco = eco.lower()
while eco == eco:
    eco = input('Escribe cualquier cosa: ')
    if eco == 'salir':
        print ('Has salido del programa...')
        break