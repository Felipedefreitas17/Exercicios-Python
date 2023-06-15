'''
Titulo: Ano em que faço 80 anos
Data: 02/03/2023
Autor: Felipe
Descrição: A partir da idade informada pelo usuário
o sistema calcula em que ano a pessoa faz 80 anos
'''
print('Bem vindo ao programa "Ano em que faço 80 anos"')
print('Por favor, informe sua idade')
idade = int(input())
ano_atual = 2023
ano_com_80_anos = 80 - idade + ano_atual

print('O ano no qual você fará 80 anos será ' +
      str(ano_com_80_anos))
