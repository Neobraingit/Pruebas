from Anonimator import Reproductor
from Anonimator import Lector
from Anonimator import Print


print ('''  /$$$$$$                                /$$                           /$$                        
 /$$__  $$                              |__/                          | $$                        
| $$  \ $$ /$$$$$$$   /$$$$$$  /$$$$$$$  /$$ /$$$$$$/$$$$   /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ 
| $$$$$$$$| $$__  $$ /$$__  $$| $$__  $$| $$| $$_  $$_  $$ |____  $$|_  $$_/   /$$__  $$ /$$__  $$
| $$__  $$| $$  \ $$| $$  \ $$| $$  \ $$| $$| $$ \ $$ \ $$  /$$$$$$$  | $$    | $$  \ $$| $$  \__/
| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$| $$ | $$ | $$ /$$__  $$  | $$ /$$| $$  | $$| $$      
| $$  | $$| $$  | $$|  $$$$$$/| $$  | $$| $$| $$ | $$ | $$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$      
|__/  |__/|__/  |__/ \______/ |__/  |__/|__/|__/ |__/ |__/ \_______/   \___/   \______/ |__/      
                                                                                                  
                                                                                                  
                                                                                                  
''')


print ('Escoge una opción ',
       'Reproductor','-','Lector','-','Imprimir')
opcion = input('Opción: ')

if opcion == 'Reproductor':
    reproductor()
elif opcion == 'Lector':
    Lector()
elif opcion == 'Imprimir':
    Imprimir()
else:
    print ('No has elegido bien')


