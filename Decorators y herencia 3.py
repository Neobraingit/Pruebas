class Colegio():
    def __init__(self, claustro, alumnos, nombre):
        self.claustro = claustro
        self.alumnos = alumnos
        self.nombre = nombre

    def modificar_alumnos(self, alumnos_nuevos):
        if alumnos_nuevos > alumnos:
            self.alumnos = alumnos_nuevos

    def resumen(self):
        print ('Claustro: ', self.claustro,
               '\nAlumnos: ', self.alumnos,
               '\nNombre: ', self.nombre)

    def midecorador(func):
        def wrapper():
            print ('Antes de la función...')
            func()
            print ('Después de la funcion...')
        return wrapper

    @midecorador
    def principal ():
        print ('Infantil')

    principal()

class Clases (Colegio):
    def __init__(self, claustro, alumnos, nombre):
        super().__init__(claustro,alumnos,nombre)

centro = Colegio(13, 25, 'Federico García Lorca')
print(centro.nombre)
centro.resumen()
clase = Clases(13, 25, 'repollos')
clase.resumen()

