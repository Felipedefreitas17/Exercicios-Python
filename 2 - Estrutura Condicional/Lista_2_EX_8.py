titulo = 'Caixa Eletrônico'
'''
Data: 07/03/2023
Autor: Felipe
Descrição: A partir de um valor, informa o usuário
o menor número de cédulas que ele precisa sacar
'''
print('Bem vindo ao programa ' + titulo)

print('Por favor, informe quanto você quer sacar')

valor = int(input())

cedulas_200 = valor // 200
valor = valor - cedulas_200*200
cedulas_100 = valor // 100
valor = valor - cedulas_100*100
cedulas_50 = valor // 50
valor = valor - cedulas_50*50
cedulas_20 = valor // 20
valor = valor - cedulas_20*20
cedulas_10 = valor // 10
valor = valor - cedulas_10*10
cedulas_5 = valor // 5
valor = valor - cedulas_5*5
cedulas_2 = valor // 2
valor = valor - cedulas_2*2
cedulas_1 = valor
total = (cedulas_200 * 200) +\
    (cedulas_100 * 100) + (cedulas_50 * 50) +\
    (cedulas_20 * 20) + (cedulas_10 * 10) +\
    (cedulas_5 * 5) + (cedulas_2 * 2) +\
    cedulas_1

print('Valor informado: R$' + str(total) + ',00')
if cedulas_200 > 0:
    print('Cedulas de R$200,00 : ' + str(cedulas_200))
if cedulas_100 > 0:
    print('Cedulas de R$100,00 : ' + str(cedulas_100))
if cedulas_50 > 0:
    print('Cedulas de R$50,00 : ' + str(cedulas_50))
if cedulas_20 > 0:
    print('Cedulas de R$20,00 : ' + str(cedulas_20))
if cedulas_10 > 0:
    print('Cedulas de R$10,00 : ' + str(cedulas_10))
if cedulas_5 > 0:
    print('Cedulas de R$5,00 : ' + str(cedulas_5))
if cedulas_2 > 0:
    print('Cedulas de R$2,00 : ' + str(cedulas_2))
if cedulas_1 > 0:
    print('Cedulas de R$1,00 : ' + str(cedulas_1))