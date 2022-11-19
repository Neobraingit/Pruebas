from playsound import playsound
def reproductor():
    print ('Opciones:\n',
           '1) Escuchar audio 1\n',
           '2) Escuchar audio 2\n',
           '3) Escuchar audio 3')
    opcion = input('Escoge una opción para escuchar música: ')
    if opcion == '1':
        archivo1 = 'audio1.mp3'
        playsound(archivo1)
    elif opcion == '2':
        archivo2 = 'audio2.mp3'
        playsound(archivo2)
    elif opcion == '3':
        archivo3 = 'audio3.mp3'
        playsound(archivo3)
    else:
        print ('Adios, buen día')


