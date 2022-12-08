'''
Programar una función que determine si una empresa es microempresa o no (retorno booleano –True o False–).
 Se dice que es microempresa si tiene menos de 50 empleados,
  factura menos de 30 milones de euros y tiene un balance igual o inferior a los 5 millones de euros.
'''
def empresa_microempresa(num1, num2, num3):
    if num1 < 50 and num2 < 30 and num3 < 5:
        print ('Es microempresa')
    else:
        print ('No es microempresa')

empresa_microempresa(49, 22, 4)
