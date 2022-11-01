class Coche ():
    def __init__(self, modelo, marca, caballos):
        self.modelo = modelo
        self.marca = marca
        self.caballos = caballos


    def escpecificaciones(self):
        print ('Modelo: ', self.modelo,
               '\nMarca: ', self.marca,
               '\nCaballos: ', self.caballos)


    def midecorador(func):
        def envoltorio():
            print ('antes de la función')
            func()
            print ('Despues de la función')
        return envoltorio

    @midecorador
    def funcion():
        print ('Dentro de la función')
    funcion()


class electrico (Coche):
    def __init__(self, modelo, marca, caballos):
        super().__init__(modelo, marca, caballos)

Toyota = electrico('Chr', 'Toyota', 122)
Toyota.escpecificaciones()
print (Toyota.marca)



