contraseña = 'Pepitogrillo'
usuario = 'Admin'
user = input('Introduce tu ususario: ')
passwd = input('Introduce tu contraseña: ')


contador = 0
while  passwd != contraseña and user != usuario :
    print ('Contraseña o usuario incorrecto¡¡')
    user = input('Introduce tu ususario: ')
    passwd = input('Introduce tu contraseña: ')
    contador += 1
print ('Acceso conseguido¡¡¡¡')







