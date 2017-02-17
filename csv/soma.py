import csv

# teste = {'testedict': [{'valor':1},{'valor':2},{'valor':3}]}


with open('soma1.csv', encoding='utf-8') as fobj_entrada, \
        open('soma2.csv', encoding='utf-8', mode='w') as fobj_saida:
    reader = csv.reader(fobj_entrada)
    writer = csv.writer(fobj_saida)
    writer.writerow(next(reader))  # escrever cabeçalho
    dictall = {}
    nome = []
    soma = 0

    # for row in reader:

    #     if row[0] in nome:
    #         pass
    #     else:
    #         nome.append(row[0])

    # print(nome)

    for row1 in reader:
        for row1 in reader:

            if row1[0] in nome:
                pass
            else:
                nome.append(row1[0])
        print(nome)
        tmp = row1[0]
        # print(tmp)
        soma = soma + int(row1[1])
        if tmp != row1[0]:
            soma = 0
            print('testeif')
        dicttemp = {}
        # if row[0] in nome:
        dicttemp = {row1[0]: [{'total': row1[1]}, {
            'max': row1[2]}, {'min': row1[3]}, {'averege': row1[4]}]}
        # print(dicttemp)
        # print(dicttemp[row1[0]][0]['total'])
        # print('testeif')
        print(soma)
