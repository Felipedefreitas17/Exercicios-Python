titulo = 'Ano Bissexto'
'''
Data: 07/03/2023
Autor: Felipe
Descrição: Verifica se um ano é bissexto
'''
print('Bem vindo ao programa ' + titulo)

print('Por favor, informe um ano')
ano = int(input())

if ano % 4 == 0: # É divisel por quatro?
    if ano % 100 > 0: # Não é divisel por 100?
        print('Ano Bissexto')
    elif ano % 400 == 0: # É divisel por 4, por 100 e por 400?
        print('Ano Bissexto')
    else:
        print('Ano Normal')
else:
    print('Ano Normal')