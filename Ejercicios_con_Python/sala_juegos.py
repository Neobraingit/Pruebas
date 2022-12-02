edad = int(input('¿Qué edad tienes? '))
if edad < 4:
    print ('Entras gratis')
elif edad == 4 and edad < 18:
    print ('Son 5 euros')
else:
    print ('Son 10 euros')