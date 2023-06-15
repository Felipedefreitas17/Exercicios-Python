titulo = 'Par ou Impar'
'''
Data: 07/03/2023
Autor: Felipe
Descrição: Informa se um número é par ou impar
'''

print('Bem vindo ao programa ' + titulo)

print('Por favor, informe um número')
numero = int(input())

resto = numero % 2

# 0 é par e  1 é impar

if resto:
    print('O número ' + str(numero) + ' é impar')
else:
    print('O número ' + str(numero) + ' é par')