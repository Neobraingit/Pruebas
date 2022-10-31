class Persona ():
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido
        self.peso = 80


    def especificaciones (self):
        print ('Nombre: ', self._nombre,
               '\nApellido: ', self._apellido,
               '\nPeso: ', self.peso)

    def modificar_peso(self, pesonuevo):
        if pesonuevo > 80:
            self.peso = pesonuevo
        else:
            print ('Ese peso no es muy bueno...')


    def modificar_nombre(self, nombrenuevo):
        if nombrenuevo == 'David':
            self._nombre = nombrenuevo
        else:
            print ('Ese nombre no es válido....')

marcos = Persona('Marcos', 'Carmona')
marcos.especificaciones()
marcos.modificar_peso(100)
marcos.especificaciones()
marcos.especificaciones()
marcos.modificar_nombre('David')
marcos.especificaciones()