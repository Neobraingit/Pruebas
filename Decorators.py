class Coche ():
    def __init__(self, modelo, caballos, velocidad):
        self.modelo = modelo
        self.caballos = caballos
        self.velocidad = velocidad

    def especificaciones(self):
        print ('Modelo: ', self.modelo,
               '\nCaballos: ', self.caballos,
               '\nVelocidad: ', self.velocidad)
    def modificar_ruedas(self,ruedas):
       if ruedas == 4:
        print ('Ese es buen número¡¡')
       else:
         print('No puede tener ese número de ruedas....')

    def mi_decorador(func):
        def wrapper():
            print('Antes de la función')
            func()
            print('Después de la función')

        return wrapper

    @mi_decorador
    def principal():
        print('Dentro de la función')

    principal()

    principal()




class Electrico(Coche):
    def __init__(self, modelo, caballos, velocidad):
        super().__init__(modelo, caballos, velocidad)

Toyota = Electrico('CHR', 122, 240)
Toyota.especificaciones()
Toyota.modificar_ruedas(67)
print (Toyota.velocidad)




