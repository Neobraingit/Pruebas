print ('Dime tu correo electrónico: ')
correo = input()
print (correo[:correo.find('@')] + '@ceu.es')