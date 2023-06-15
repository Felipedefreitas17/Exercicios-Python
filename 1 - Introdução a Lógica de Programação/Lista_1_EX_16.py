'''
Titulo: Calculo de IMC
Data: 02/03/2023
Autor: Felipe
Descrição: Calcula o IMC e faz cadastro de usuário
'''
print('Bem vindo ao programa de calculo de IMC')
print('Por favor, informe seu nome')
nome = input()
print('Informe sua idade')
idade = int(input())
print('Informe seu peso em Kg')
peso = float(input())
print('Informe seu altura em metros')
altura = float(input())

num_caracteres = len(nome)

ano_nasc = 2023 - idade

altura_em_cm = altura * 100

imc = peso / (altura * altura)

print('Seu nome é ' + nome +
      ' e tem ' + str(num_caracteres) +
      ' caracteres, você tem ' + str(idade) +
      ' anos e nasceu no ano de ' + str(ano_nasc) +
      '. Você mede ' + str(altura_em_cm) +
      ' cm, pesa ' + str(peso) +
      ' Kg e seu IMC é: ' + str(imc) + '.')
