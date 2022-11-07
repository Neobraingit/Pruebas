class Colegio():
    def __init__(self, nombre, especiañlidad):
        self.nombre = nombre
        self.especialidad = especiañlidad

    def características(self):
        print ('Nombre: ', self.nombre,
               '\nEspecialidad: ', self.especialidad)



class Maestros(Colegio):
    def __init__(self, nombre, especialidad):
        super().__init__(nombre, especialidad)


Eva = Maestros ('Eva', 'Infantil')

Eva.características()