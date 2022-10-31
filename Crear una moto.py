class Moto ():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ruedas = 2

    def especificaciones(self):
        print ('Marca: ', self.marca,
               '\nModelos: ', self.modelo,
               '\nRuedas: ', self.ruedas)

    def modificar_marca(self, modimarca):
        if modimarca != 'Yamaha':
            self.marca = modimarca

    def modificar_modelo(self, modimodelo):
        if modimodelo != 'T-max':
            self.marca = modimodelo


escooter = Moto('Yamaha', 'T-max')
print (escooter.marca)
escooter.especificaciones()
escooter.modificar_marca('Suzuki')
escooter.especificaciones()
escooter.modificar_modelo('Vespa')
escooter.especificaciones()
