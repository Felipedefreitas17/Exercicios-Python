titulo = 'Gratuidade no transporte'
'''
Data: 07/03/2023
Autor: Felipe
Descrição: Verifica se uma pessoa tem 65 anos ou mais
'''
print('Bem vindo ao programa ' + titulo)

print('Por favor, informe a idade')
idade = int(input())

if idade >= 65:
    print('Você tem gratuidade no transporte')
else:
    print('Você não tem gratuidade no transporte')