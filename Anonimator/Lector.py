import csv
def Lector():
    print ('Vamos a leer un csv')
    file = open('Biblioteca.csv')
    reader = csv.reader(file)
    for row in reader:
        print (row)

