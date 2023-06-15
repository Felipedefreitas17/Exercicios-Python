titulo = 'Organização de Str'
'''
Data: 17/03/2023
Autor: Felipe
Descrição: Programa para popular uma lista
a partir de uma string
'''
print('Bem vindo ao programa ' + titulo + '\n')

pessoas = '''jose
jorge
maria
antonio
ana
julia
márcio
fernando
zelia'''

lista_pessoas = pessoas.split('\n')
print(lista_pessoas)

for indice, pessoa in enumerate(lista_pessoas,start=1):
    print(indice,'-',pessoa)