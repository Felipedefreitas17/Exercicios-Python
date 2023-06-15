titulo = 'Lançador de 2 dados'
'''
Data: 10/03/2023
Autor: Felipe
Descrição: Joga dois dados o número de vezes que for
decidido
'''
print('Bem vindo ao programa ' + titulo)

import random

print('Este programa joga dois dados')
print('Digite o número de vezes que o programa \
irá lançar dois dados')

numero_vezes = int(input())

resultado2 = 0
resultado3 = 0
resultado4 = 0
resultado5 = 0
resultado6 = 0
resultado7 = 0
resultado8 = 0
resultado9 = 0
resultado10 = 0
resultado11 = 0
resultado12 = 0


for jogada in range(numero_vezes):
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)

    dado_total = dado1 + dado2

    if dado_total == 2:
        resultado2 += 1
    elif dado_total == 3:
        resultado3 += 1
    elif dado_total == 4:
        resultado4 += 1
    elif dado_total == 5:
        resultado5 += 1
    elif dado_total == 6:
        resultado6 += 1
    elif dado_total == 7:
        resultado7 += 1
    elif dado_total == 8:
        resultado8 += 1
    elif dado_total == 9:
        resultado9 += 1
    elif dado_total == 10:
        resultado10 += 1
    elif dado_total == 11:
        resultado11 += 1
    elif dado_total == 12:
        resultado12 += 1

print('dado 2: ' + str(resultado2))
print('dado 3: ' + str(resultado3))
print('dado 4: ' + str(resultado4))
print('dado 5: ' + str(resultado5))
print('dado 6: ' + str(resultado6))
print('dado 7: ' + str(resultado7))
print('dado 8: ' + str(resultado8))
print('dado 9: ' + str(resultado9))
print('dado 10: ' + str(resultado10))
print('dado 11: ' + str(resultado11))
print('dado 12: ' + str(resultado12))









