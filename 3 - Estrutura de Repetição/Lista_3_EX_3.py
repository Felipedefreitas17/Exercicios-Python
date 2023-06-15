import random
from time import sleep

titulo = 'Pedra, Papel e Tesoura'
'''
Data: 10/03/2023
Autor: Felipe
Descrição: Jogo de Pedra, Papel e Tesoura
'''
print('Bem vindo ao programa ' + titulo)
sleep(1)
num_vit = 0
num_der = 0
num_emp = 0
print('\n'+'-'*50+'\n')
sleep(0.5)
while True:
    print('Escolha Pedra (R), Papel (P), Tesoura (T) \
ou (X) para sair do jogo')
    escolha_usuario = input().upper()

    if escolha_usuario == 'X':
        print('Jogo Finalizado')
        sleep(1)
        break
    elif escolha_usuario != 'R' and\
        escolha_usuario != 'P' and\
        escolha_usuario != 'T':
        print('Você digitou uma letra inválida')
        sleep(1)
        continue
    sleep(1)
    print('Você jogou... ',end='')
    sleep(1)
    if escolha_usuario == 'R':
        print('Pedra')
    elif escolha_usuario == 'P':
        print('Papel')
    else:
        print('Tesoura')

    escolha_pc = random.randint(1,3)
    print('O PC jogou... ', end='')
    if escolha_pc == 1:
        escolha_pc = 'R'
        print('Pedra')
    elif escolha_pc == 2:
        escolha_pc = 'P'
        print('Papel')
    else:
        escolha_pc = 'T'
        print('Tesoura')
    sleep(1)


    sleep(1)
    print('Resultado do Turno: ',end ='')
    sleep(2)
    if escolha_usuario == 'R':
        if escolha_pc == 'R':
            print('Empate')
            num_emp += 1
        elif escolha_pc == 'P':
            print('Você Perdeu')
            num_der += 1
        else:
            print('Você Ganhou')
            num_vit += 1
    elif escolha_usuario == 'P':
        if escolha_pc == 'R':
            print('Você Ganhou')
            num_vit += 1
        elif escolha_pc == 'P':
            print('Empate')
            num_emp += 1
        else:
            print('Você Perdeu')
            num_der += 1
    elif escolha_usuario == 'T':
        if escolha_pc == 'R':
            print('Você Perdeu')
            num_der += 1
        elif escolha_pc == 'P':
            print('Você Ganhou')
            num_vit += 1
        else:
            print('Empate')
            num_emp += 1
    sleep(2)
    print('\n' + '-' * 50 )
    sleep(0.5)
    print('Vitorias: ' + str(num_vit))
    sleep(0.5)
    print('Derrotas: ' + str(num_der))
    sleep(0.5)
    print('Empates: ' + str(num_emp))
    sleep(0.5)
    print('-' * 50 + '\n')
    sleep(1)
