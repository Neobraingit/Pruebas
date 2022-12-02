payaso = 112
muñeca = 75
print ('¿Cuántos payasos vas a enviar? ')
numpayasos = int(input())
print ('¿Cuántas muñecas vas a enviar? ')
nummuñecas = int(input())

peso_payasos = payaso * numpayasos
peso_muñecas = muñeca * nummuñecas
peso_total_paquete = peso_muñecas * peso_payasos
print (peso_total_paquete)