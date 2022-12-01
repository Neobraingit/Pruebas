'''
Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
'''

def max_de_tres(n1, n2, n3):
    if n1 > n2 and n3:
        print (n1)
    elif n2 > n1 and n3:
        print (n2)
    else:
        print (n3)

max_de_tres(3, 4, 5)