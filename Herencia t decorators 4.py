class Persona():
    def __init__(self, edad, sexo, raza):
        self.edad = edad
        self.sexo = sexo
        self.raza = raza
        self.altura = 1.80

    def caracteristicas(self):
        print ('Edad: ', self.edad,
               '\nSexo: ', self.sexo,
               '\nRaza: ', self.raza)

    def modificar_altura(self, altura_nueva):
        if altura_nueva > 1.80:
            self.altura = altura_nueva
        else:
            print ('Es más bajo que la altura media')

    def midecorador(func):
        def wrapper():
            print ('Dentro de la función')
            func()
            print ('Fuera de la función')
        return wrapper

    @midecorador
    def funcion():
        print ('En medio de la función')

    funcion()


class Niño(Persona):
    def __init__(self, edad,sexo,raza):
        super().__init__(edad, sexo,raza)

Marcos = Niño(12, 'varón', 'caucásico')
Marcos.caracteristicas()
Marcos.modificar_altura(1.79)
Marcos.caracteristicas()
Marcos.modificar_altura(1.79)
