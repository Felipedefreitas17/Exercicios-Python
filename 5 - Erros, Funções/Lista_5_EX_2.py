titulo = 'Apelido'
'''
Data: 23/03/2023
Autor: Felipe
Descrição: Tranforma o nome em um apelido
'''
print('Bem vindo ao programa ' + titulo + '\n')

def criador_de_apelido(_nome):
    return _nome[:3] + _nome[-3:]



apelido = criador_de_apelido(input('Digite seu nome completo: '))
print(apelido)