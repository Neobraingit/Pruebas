print(''' _______  _______  _______  _______  _______  _        _______ 
(  ____ )(  ____ \(  ____ )(  ____ \(  ___  )( (    /|(  ___  )
| (    )|| (    \/| (    )|| (    \/| (   ) ||  \  ( || (   ) |
| (____)|| (__    | (____)|| (_____ | |   | ||   \ | || (___) |
|  _____)|  __)   |     __)(_____  )| |   | || (\ \) ||  ___  |
| (      | (      | (\ (         ) || |   | || | \   || (   ) |
| )      | (____/\| ) \ \__/\____) || (___) || )  \  || )   ( |
|/       (_______/|/   \__/\_______)(_______)|/    )_)|/     \|
                                                               
                            by Marcos Carmona García ''')
class Persona ():
    '''Esto es la clase Persona'''
    def __init__(self, nombre, apellido, edad, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
        self.peso = 95

    def características(self):
        print ('Nombre: ', self.nombre,
               '\nApellido: ', self.apellido,
               '\nEdad: ',self.edad,'años',
               '\nSexo: ', self.sexo)

    def modificarpeso(self, peso):
        if peso > 95:
            print ('Estás muy gordo¡¡¡')
        else:
            print ('Estás bien de peso¡¡')

    def modificarsexo(self, sexo):
        if sexo == 'hombre':
            print ('Eres un hombre...')
        else:
            print ('Eres una mujer...')

class Niño(Persona):
    def __init__(self, nombre,apellido,edad,sexo):
        super().__init__(nombre,apellido,edad,sexo)

'''Vamos a hacer un bucle for'''
texto = 'Me llamo Marcos Carmona García'
letra = input('Introduce una letra: ')
count = 0
for i in texto:
    if i in letra:
        count += 1
        print (count)
