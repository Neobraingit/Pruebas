from playsound import playsound

pregunta = input('¿Te apetece escuchar una canción?')
if pregunta == 'si':
    archivo = 'audio.mp3'
    playsound((archivo))
else:
    print ('Eres muy aburrido¡¡¡')