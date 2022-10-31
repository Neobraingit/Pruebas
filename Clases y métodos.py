# Definiendo una clase
class Casa():
    '''Esto crea una casa'''
    def __init__(self, altura, color):
        '''altura == float
           color == str'''
        self._altura = altura
        self._color = color
        self._peso = 1000

    def modificar_peso(self,peso):
        '''Esto modifica el peso'''
        if peso > self._peso:
            self._peso = peso
        else:
            print('El peso no es correcto...')

    def modificar_color(self, colores):
        '''Esto modifica el color siempre que sea Naranja'''
        if colores == 'Naranja':
            self._color = colores
        else:
            print ('Color no válido...')

    def modificar_altura(self, alturacasa):
        ''' Esto modifica la altura'''
        if alturacasa > 2.0:
            self._altura = alturacasa



    def especificaciones(self):
        print ('Altura: ', self._altura,
               '\nColor: ', self._color,
               '\nPeso: ', self._peso)




apartamento = Casa(2.0 , 'rojo')
apartamento.especificaciones()
apartamento.modificar_peso(4000)
apartamento.modificar_color('Naranja')
apartamento.modificar_altura(4.0)
apartamento.especificaciones()

