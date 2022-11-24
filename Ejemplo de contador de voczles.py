

ini = True

while ini:
    les = input('Escribe algo y se contarán las vocales ')
    a = les.count('a')
    e = les.count('e')
    i = les.count('i')
    o = les.count('o')
    u = les.count('u')
    print('Tu enunciado tiene:\n', str(a),
          'a\'s\n', str(e), 'e\'s\n', str(i), 'i\'s\n',
          str(o), 'o\'s\n', str(u), 'u\'s\n')