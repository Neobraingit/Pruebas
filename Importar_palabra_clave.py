print ('Menú:',
       '\n1) Importar palabra',
       '\n2) Mostrar palabra')

fichero = open('Importar.txt', 'w')
fichero.write('Esto es un listado de palabras clave: '
              '\nCebolla'
              '\nAjo')
fichero.close()



