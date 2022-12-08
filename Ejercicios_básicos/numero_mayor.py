'''
Función que retorne el mayor de dos números o 0 si son iguales
'''
def numero_mayor(num1, num2):
    if num1 > num2:
        print (num1,'es mayor')
    elif num2 > num1:
        print (num2,'es mayor')
    else:
        print (0)

numero_mayor(4,2)