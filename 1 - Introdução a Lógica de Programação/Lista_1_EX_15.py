'''
Titulo: Calculo de Média
Data: 02/03/2023
Autor: Felipe
Descrição: Calcula a média de duas notas informadas
pelo usuário
'''
print('Bem vindo ao programa de calcular média')
print('Por favor, informe sua primeira nota')
nota_1 = float(input())
print('Informe sua segunda nota')
nota_2 = float(input())

media = (nota_1 + nota_2) / 2

print('Sua média será ' + str(media))