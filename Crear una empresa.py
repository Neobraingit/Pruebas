class Adriastur ():
    def __init__(self, operarios, categoría):
        self._operarios = operarios
        self._categoría = categoría
        self._metros = 100

    def plantilla (self):
        print ('Operarios: ', self._operarios,
               '\nCategoría: ', self._categoría,
               '\nMetros mínimos: ', self._metros)

    def modificar_metros (self, añadirmetros):
        if añadirmetros > 100:
            print ('Eres un fenómeno¡¡¡¡')
        else:
            print ('No rindes....')




Marcos = Adriastur('Marcos', 'Oficial de 1º')
print (Marcos.plantilla())
Marcos.modificar_metros(300)
print (Marcos.plantilla())



