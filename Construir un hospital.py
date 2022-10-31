class Hospital():
    '''Creamos un hospital'''
    def __init__(self, Nombre, Dirección):
     self.Nombre = Nombre
     self.Dirección = Dirección
     self.enfermedad = 'Cáncer'



    def Especialidad (self, especialidad):
        print ('La especialidad es: ')

    def Información (self):
        print ('Nombre:', self.Nombre,
               '\nDirección: ', self.Dirección,
               '\nEnfermedad: ', self.enfermedad)

    def modificar_enfermedad(self, enfermedad):
        if enfermedad == 'Gripe':
            self.enfermedad = enfermedad

enfermo = Hospital('Cabueñes', 'Jove')
enfermo.Especialidad('Pediatría')
enfermo.Información()
enfermo.modificar_enfermedad('Gripe')
enfermo.Información()


