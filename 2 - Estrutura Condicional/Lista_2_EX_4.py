titulo = 'Promoção Otica'
'''
Data: 07/03/2023
Autor: Felipe
Descrição: Faz uma promoção de óculos
de acordo com a idade
'''
print('Bem vindo ao programa ' + titulo)

print('-'*10 + 'OTICAS OLHO BOM' + '-'*10)

valor_do_oculos = 200

print('Promoção especial no óculos de R$' +
      str(valor_do_oculos) + ',00')
print('Informe sua idade para saber o desconto')
idade = int(input())

desconto = idade

if desconto > 80:
    desconto = 80
elif desconto < 10:
    desconto = 10

desconto_em_reais = desconto * valor_do_oculos/100

valor_final = valor_do_oculos - desconto_em_reais

print('Você tem ' + str(idade) + ' anos e ganhou um \
desconto de ' + str(desconto) + '%')
print('O óculos sairá por apenas ' + str(valor_final) +
      ' reais')