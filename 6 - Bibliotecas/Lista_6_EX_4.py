titulo = 'Lista de Compras com CSV'
'''
Data: 29/03/2023
Autor: Felipe
Descrição: Cria uma lista de compras com a possibilidade
de adicionar, remover, listar itens e salvar lista (em csv)
'''
print('Bem vindo ao programa ' + titulo + '\n')

import csv
import time

time.sleep(0.5)
compras = []
try:
    with open('Arquivos/compras.csv','r',) as file:
        reader = csv.reader(file)
        for linha in reader:
            compras.append(linha)
except:
    print('Lista de compras não encontrada')
    print('Será criado uma nova lista\n')
time.sleep(0.5)
while True:
    print('''#############################################
Digite (I) para incluir um item na lista,
Digite (D) para deletar um item da lista,
Digite (L) para listar os valores,
Digite (S) para salvar a lista em csv,
Digite (X) para encerrar o programa.
#############################################\n''')
    time.sleep(0.5)
    escolha = input().upper()

    while escolha == 'I':
        print('\nDigite um Item para incluir ou (Q) para voltar')
        time.sleep(0.2)
        item = input('Item: ').upper()
        time.sleep(0.2)
        if item == 'Q':
            escolha = ''
            break
        else:
            quant = input('Quantidade: ')
            time.sleep(0.2)
            lista_item = []
            lista_item.append(item)
            lista_item.append(quant)
            compras.append(lista_item)

    if escolha == 'X':
        time.sleep(0.2)
        print('Encerrando o programa')
        time.sleep(1)
        break
    elif escolha == 'D':
        for indice, valor in enumerate(compras,start=1):
            print(indice,'-',valor)
        item = int(input('Indice do Item a ser deletado: '))
        deletado = compras.pop(item-1)
        print('\nO item',deletado,'foi deletado\n')
    elif escolha == 'L':
        time.sleep(0.2)
        print('\n################################')
        print('Lista de Compras (arquivo csv)')
        time.sleep(0.2)
        try:
            with open('Arquivos/compras.csv','r') as file:
                reader = csv.reader(file)
                for linha in reader:
                    print(linha[0],'-',linha[1])
                    time.sleep(0.2)
        except:
            print('Arquivo CSV não encontrado')
            time.sleep(0.2)
        print('################################\n')
        time.sleep(0.5)
        print('\n################################')
        print('Lista de Compras (atual)')
        time.sleep(0.2)
        for linha in compras:
            print(linha[0],'-',linha[1])
            time.sleep(0.2)
        print('################################\n')
    elif escolha == 'S':
        time.sleep(0.2)
        print('Salvando Lista de Compras')
        time.sleep(0.5)
        try:
            with open('Arquivos/compras.csv','w',newline='') as file:
                writer = csv.writer(file)
                for linha in compras:
                    writer.writerow(linha)
            print('Arquivo Salvo com Sucesso\n')
        except:
            print('Erro ao salvar arquivo\n')
        time.sleep(0.5)
    elif escolha == '':
        continue
    else:
        print('Você digitou um comando incorreto')
        time.sleep(0.5)