import csv

with open('teste1.csv') as csvfile:
    #arq2 = open('teste2.csv')
    reader = csv.DictReader(csvfile)
    #writer = csv.writer(csvfile)
    lista = []
    for row in reader:
        teste = str(row['URL'])
        test2 = teste.split('/')
        #writer.writerow(['URL'], test2[1])
        print(test2[1])
        lista.append(test2[1])

print (lista)
with open('teste2.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile)
    for item in lista:
        spamwriter.writerows([item])
