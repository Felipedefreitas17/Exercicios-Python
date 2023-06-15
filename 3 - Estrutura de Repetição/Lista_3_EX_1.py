import random

numero_correto = random.randint(0,10000)

print('Bem vindo ao jogo de adivinhação')
print('Descubra que número estou pensando de 0 a 10000')
print('Você terá 10 tentativas')

for tentativa in range(10):
    print('tentativa: ' + str(tentativa+1))

    print('Digite um número')
    numero = int(input())

    if numero == numero_correto:
        print('Você ganhou')
        break
    elif numero < numero_correto:
        print('O número é maior')
    elif numero > numero_correto:
        print('O número é menor')