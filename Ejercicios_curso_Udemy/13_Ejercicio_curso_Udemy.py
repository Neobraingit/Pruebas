'''
Crea un diccionario con los siguientes pares de valores:
  manzana : apple
  naranja : orange
  plátano : banana
  limón : lemon
Muestra la traducción para la palabra 'naranja'
Añade un nuevo elemento con 'piña' : 'pineaple
Haz un bucle para mostrar el diccionario
'''

frutas = {'manzana' : 'apple', 'naranja' : 'orange', 'platano' : 'banana', 'limon' : 'lemon'}
print (frutas.get('naranja'))
frutas['piña'] = 'pineaple'
print (frutas)
while frutas:
    print (frutas)
    break