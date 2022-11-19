import csv
file = open('Biblioteca.csv')
reader = csv.reader(file)
for row in reader:
    print (row)