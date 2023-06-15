'''
Titulo: Calculadora de Latas de Tinta
Data: 02/03/2023
Autor: Felipe
Descrição: Calcula quantas latas de tinta o
usuário precisará utilizar de acordo com a largura
e altura de sua parede
'''

print('Bem vindo ao programa de calculo de Latas de Tinta')

print('Por favor, informe a largura da sua parede')
largura = float(input())
print('Informe a altura da sua parede')
altura = float(input())

area = largura * altura
area_lata = 3

latas = area // area_lata
resto_latas = int(area % area_lata > 0)
latas_final = int(latas + resto_latas)

print('Você precisará de ' + str(latas_final) +
      ' latas para cobrir sua parede')
