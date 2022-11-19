from Anonimator.Reproductor import *
from Anonimator.Lector import  *
from Anonimator.Print import *
import Anonimator

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


