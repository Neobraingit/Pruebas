class Dibujo ():
    '''Esta será la clase padre'''
    def __init__(self, estilo, pintor):
        self.estilo = estilo
        self.pintor = pintor



    def disciplina(self):
        print ('Estilo: ', self.estilo,
               '\nPintor: ', self.pintor)

    def modificar_estilo(self, estilonuevo):
        if estilonuevo != 'realista':
            self.estilo = estilonuevo
    def modificar_pintor(self, pintornuevo):
        if pintornuevo != 'Van Goth':
            self.pintor = pintornuevo

class Eva (Dibujo):
    def __init__(self, estilo, pintor, colores):
        super().__init__(estilo, pintor)
        self.colores = colores
artista = Eva('realista', 'Van Goh', 'Rojo')
artista.disciplina()
artista.modificar_pintor('Velazquez')
artista.disciplina()

class Coche():
    def __init__(self,modelo, caballos, velocidad):
        self.modelo = modelo
        self.caballos = caballos
        self.velocidad = velocidad

    def especificaciones(self):
        print ('Modelo: ', self.modelo,
               '\nCaballos: ', self.caballos,
               '\nVelocidad: ', self.velocidad)


seat = Coche('marbella', 180, 230)
seat.especificaciones()

class electrico(Coche):
    def __init__(self, modelo, caballos, velocidad):
        super().__init__(modelo, caballos, velocidad)

Toyota = electrico('Ch-r', 122, 230)
Toyota.especificaciones()













    
        







