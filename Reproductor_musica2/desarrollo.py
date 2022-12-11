def reproducir ():
    from playsound import playsound
    print ('Opciones:',
           '\n Opción 1',+
           '\n Opción 2')
    opcion = input('Escoge la opción: ')
    if opcion == '1':
        archiuvo2 = 'Iron_Maiden.mp3'
        playsound(archiuvo2)    
        
reproducir()