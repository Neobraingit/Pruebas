dict = {'Euro' : 'e', 'Dolar' : '$', 'Yen' : 'y'}
monedas = input('Dime tu divisa: ')
print (dict.get(monedas.title(), 'La divisa no está'))