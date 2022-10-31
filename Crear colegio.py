class Colegio ():
    '''Crea la clase Colegio'''
    def __init__(self, Especialidad, dirección, jefe_de_estudios):
        self.Especialidad = Especialidad
        self.dirección = dirección
        self.jefe_de_estudios = jefe_de_estudios
        self.niños = 25

    def claustro(self):
        print ('Profesores: ', self.Especialidad,
               '\nDirección: ', self.dirección,
               '\nJefe de estudios: ', self.jefe_de_estudios,
               '\nNiños: ', self.niños)

    def modificar_niños (self, nuevos):
        if nuevos != 0:
            self.niños = nuevos


Eva = Colegio('Infantil', 'Juan', 'María')
print (Eva.Especialidad)
print (Eva.niños)
Eva.claustro()
Eva.modificar_niños(55)
Eva.claustro()
Eva.claustro()