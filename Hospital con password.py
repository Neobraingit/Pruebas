class Hospital():
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def validacion_de_usuario():
        usuario = 'Admin'
        contraseña = 'Pepitogrillo'
        user = input('Introduce un usuario: ')
        passwd = input('introduce una contraseña: ')
        contador = 0
        while user != usuario and passwd != contraseña:
            print ('Contraseña o usuario incorrectos''')
            contador += 1
            user = input('Introduce un usuario: ')
            passwd = input('Introduce una contraseña: ')
        acceso = print ('Acesso conseguido¡¡')








medico = Hospital
medico.validacion_de_usuario()














