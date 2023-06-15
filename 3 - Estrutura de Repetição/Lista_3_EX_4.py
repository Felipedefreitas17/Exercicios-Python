import random
import time

titulo = 'Jogo de Luta'
'''
Data: 13/03/2023
Autor: Felipe
Descrição: Jogo de Luta entre usuario e PC
'''
print('Bem vindo ao programa ' + titulo + '\n')

time.sleep(1)
vida_usuario = 10
vida_pc = 10

# Loop Principal do Jogo
while True:
    # Verifica a escolha do usuário
    print('Escolha (A) para Soco, (B) para cabeçada \
e (X) para Sair')
    escolha_usuario = input().upper()

    time.sleep(1)
    # Define o que cada escolhe irá fazer
    if escolha_usuario == 'A': # Trata como Soco
        print('Você escolheu soco')
        poder_usuario = random.randint(1,6)
        dano_usuario = random.randint(1,6)
    elif escolha_usuario == 'B': # Trata como Cabeçada
        print('Você escolheu cabeçada')
        poder_usuario = 3
        dano_usuario = 3
    elif escolha_usuario == 'X': # Encerra o Jogo
        print('Encerrando o jogo')
        time.sleep(1)
        break
    else: # Escolha incorreta, retorna o inicio do while
        print('Você escolheu uma opção errada')
        time.sleep(1)
        continue

    # Anota o poder e dano do PC
    poder_pc = random.randint(1,6)
    dano_pc = random.randint(1,6)

    time.sleep(1)
    # Imprime as informações de combate
    print('Seu poder é: ' + str(poder_usuario))
    print('Seu oponente tem poder: ' + str(poder_pc))

    time.sleep(1)
    # Define quem ganhou o turno
    if poder_usuario > poder_pc:
        print('Você ganhou o combate')
        time.sleep(1)
        print('Você desferiu ' + str(dano_usuario) + ' de dano')
        vida_pc -= dano_usuario
        if escolha_usuario == 'B':
            time.sleep(1)
            print('Você recebeu 1 de dano')
            vida_usuario -= 1
    elif poder_usuario < poder_pc:
        print('Você perdeu o combate')
        time.sleep(1)
        print('Você recebeu ' + str(dano_pc) + ' de dano')
        vida_usuario -= dano_pc
    else:
        print('Este turno empatou')

    time.sleep(1)
    print('-'*30)
    # Informa a vida atual dos dois participantes
    print('Vida_Usuário: ' + str(vida_usuario))
    print('Vida_PC: ' + str(vida_pc))
    print('-' * 30)
    time.sleep(1)
    # Verifica se alguém perdeu
    if vida_usuario <= 0:
        print('Você perdeu o jogo')
        time.sleep(1)
        break
    elif vida_pc <= 0:
        print('Você ganhou o jogo')
        time.sleep(1)
        break

    print('#'*50)
    time.sleep(2)