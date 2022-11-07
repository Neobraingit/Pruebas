user = 'admin'
paaswd = '123'
print ('Bienvenido, ingrese sus datos: ')
print ('Usuario: ')
usuario = input()
print ('Contraseña: ')
contraseña = input()
if usuario == user and paaswd == contraseña:
    print ('Bienvenido al programa¡¡')
else:
    print ('Usuario o contraseña no válidas¡¡')