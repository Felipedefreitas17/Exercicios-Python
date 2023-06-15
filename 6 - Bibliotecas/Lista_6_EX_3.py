titulo = 'Importar TXT, Exportar CSV'
'''
Data: 28/03/2023
Autor: Felipe
Descrição: Importa txt com uma lista de alunos com notas 1 e 2
Exporta um csv com uma lista de alunos com nota 1, nota 2 e média
'''
print('Bem vindo ao programa ' + titulo + '\n')

import csv

texto = ''
with open('Arquivos/alunos.txt','r') as file:
    texto += file.read()

lista_txt_linhas = texto.split('\n')
lista_txt_final = []
for linha in lista_txt_linhas:
    linha_table = linha.split(',')
    lista_txt_final.append(linha_table)
print(lista_txt_final)

lista_csv = []
for linha in lista_txt_final:
    media = (float(linha[1]) + float(linha[2])) / 2
    lista_linha = []
    lista_linha.append(linha[0]) # Nome
    lista_linha.append(linha[1]) # Nota 1
    lista_linha.append(linha[2]) # Nota 2
    lista_linha.append(media)
    lista_csv.append(lista_linha)
print(lista_csv)


with open('Arquivos/alunos.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Nome','Nota 1','Nota 2','Media']) # Header do CSV
    for linha in lista_csv:
        writer.writerow(linha)