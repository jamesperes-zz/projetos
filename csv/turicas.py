import csv


with open('teste1.csv', encoding='utf-8') as fobj_entrada, \
        open('teste2.csv', encoding='utf-8', mode='w') as fobj_saida:
    reader = csv.reader(fobj_entrada)
    writer = csv.writer(fobj_saida)
    writer.writerow(next(reader))  # escrever cabeçalho
    for row in reader:
        print(row)
        row[0] = row[0].split('/')[1]
        writer.writerow(row)
