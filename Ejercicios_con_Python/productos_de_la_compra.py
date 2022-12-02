cesta = input('Escribe lo que has comprado: ')
print (cesta.replace(',' , '\n'))

cesta2 = input('Escribe lo que has comprado otra vez: ')
print ('\n'.join(cesta.split(',')))
