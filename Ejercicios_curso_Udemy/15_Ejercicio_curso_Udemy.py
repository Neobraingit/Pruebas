'''
Crear una clase 'Coche' que tenga estos atributos:
marca, color, combustible y cilindrada
Crear la función __init__ que asigne los valores de la clase
Crear otra función 'mostrar_características' que me diante print muestre los atributos de la clase
Crear un pbjeto coche1 con los atributos Opel, Rojo, Gasolina, 1.6
Ejecutar la función mostrar_careacterísticas del objeto coche1
'''

class Coche:
    def __init__(self, marca, color, combustible, cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada

    def mostrar_caracteristicas(self):
        print ('El coche tiene las siguientes características:'
               '\n Marca = Opel',
               '\n Color = Rojo',
               '\n Combustible = Gasoil',
               '\n Cilindrada = 1.6')

coche1 = Coche('Opel', 'Rojo', 'Gadsolina', '1.6')
print (coche1.mostrar_caracteristicas())
print(coche1.color)
print(coche1.marca)