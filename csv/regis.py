import csv

lista = []

with open('teste1.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        teste = str(row['URL']).split('/')
        for i in teste:
            lista.append(i)
    csvfile.close

print(lista)

with open('teste2.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(lista)