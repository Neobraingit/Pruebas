from playsound import playsound
print('''  _____  ______ _____  _____   ____  _____  _    _  _____ _______ ____  _____  
 |  __ \|  ____|  __ \|  __ \ / __ \|  __ \| |  | |/ ____|__   __/ __ \|  __ \ 
 | |__) | |__  | |__) | |__) | |  | | |  | | |  | | |       | | | |  | | |__) |
 |  _  /|  __| |  ___/|  _  /| |  | | |  | | |  | | |       | | | |  | |  _  / 
 | | \ \| |____| |    | | \ \| |__| | |__| | |__| | |____   | | | |__| | | \ \ 
 |_|  \_\______|_|    |_|  \_\\____/|_____/ \____/ \_____|  |_|  \____/|_|  \_\
                                                                               
                                                                               
''')

print ('Bienvenidos a mi reprductor')
print ('Opciones:\n 1) audio1\n 2) audio2\n 3) audio3')
menu = input('''Introduce que deseas escuchar: ''')
if menu == '1':
    archivo = 'audio1.mp3'
    playsound(archivo)
elif menu == '2':
    archivo2 = 'audio2.mp3'
    playsound(archivo2)
elif menu == '3':
    archivo3 = 'audio3.mp3'
    playsound(archivo3)
else:
    print ('Adiós, buen día...')