

ini = True

while ini:
    res = input('Escribe algo y se contarÃƒÂ¡n las vocales ')
    a = res.count('a')
    e = res.count('e')
    i = res.count('i')
    o = res.count('o')
    u = res.count('u')
    print('Tu enunciado tiene:\n', str(a),
          'a\'s\n', str(e), 'e\'s\n', str(i), 'i\'s\n',
          str(o), 'o\'s\n', str(u), 'u\'s\n')