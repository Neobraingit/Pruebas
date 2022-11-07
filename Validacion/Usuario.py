def validacion_usuario():
    usuario = input('Introduce el usuario: ')
    if len(usuario) < 6 or len(usuario) > 12:
        print('El usuario no es correcto...')
    else:
        print('El usuario es correcto...')