vegetariano = ['pimiento', 'tofu']
novegetariano = ['peperoni', 'jamon', 'salmon']
pregunta = input('¿Cómo quieres la pizza? ')
if pregunta == 'vegetariana':
    print (vegetariano)
elif pregunta == 'no vegetariano':
    print (novegetariano)
ingrediente = input('Dime un ingredinete: ')
if ingrediente in vegetariano:
    print ('Te vas a comer una vegetariana...')
else:
    print ('Carnivoro¡¡¡¡')