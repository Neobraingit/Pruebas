'''
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 * la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
'''


def fibonacci(numero, anterior, step):
    print(step, "-", numero)
    if numero == 0:
        numero += 1
        step += 1
        print(step, "-", numero)
    nuevo_numero = numero + anterior
    if step != 50:
        step += 1
        fibonacci(nuevo_numero, numero, step)
    else:
        return


step = 1
numero = 0
anterior = 0

fibonacci(4,3,1)

