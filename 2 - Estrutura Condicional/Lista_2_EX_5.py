titulo = 'Reajuste Salarial'
'''
Data: 07/03/2023
Autor: Felipe
Descrição: Faz o reajuste salarial do usuário com
base na tabela:
•	Salário Abaixo de R$1.500,00  Aumento de 25%
•	Salário Entre de R$1.500,00 e R$1.999,99  Aumento de 20%
•	Salário Entre de R$2.000,00 e R$2.999,99  Aumento de 15%
•	Salário Entre de R$3.000,00 e R$4.999,99  Aumento de 10%
•	Salário Acima de R$5.000,00  Aumento de 5%
'''
print('Bem vindo ao programa ' + titulo)

print('Por favor, informe seu salario atual')

salario_atual = float(input())

if salario_atual < 1500:
    reajuste = 25
elif salario_atual < 2000:
    reajuste = 20
elif salario_atual < 3000:
    reajuste = 15
elif salario_atual < 5000:
    reajuste = 10
else:
    reajuste = 5

aumento = salario_atual * reajuste / 100

salario_final = salario_atual + aumento

print('Seu salário atual é ' + str(salario_atual)
      + str(' reais'))
print('Você ganhará ' + str(reajuste) + '% de aumento')
print('O valor do aumento será ' + str(aumento)
      + ' reais')
print('Seu salário final será ' + str(salario_final)
      + ' reais')