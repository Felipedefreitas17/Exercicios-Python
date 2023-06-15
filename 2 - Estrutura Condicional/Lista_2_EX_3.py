titulo = 'Validação de média'
'''
Data: 07/03/2023
Autor: Felipe
Descrição: Valida se o usuário está aprovado após
solicitar duas notas

OBS:
> 7 ---> Aprovado
< 5 ---> Reprovado
Entre 5 e 7 ---> Recuperação
'''

print('Bem vindo ao programa ' + titulo)

print('Por favor, informe a primeira nota')
nota1 = float(input())

print('Informe a segunda nota')
nota2 = float(input())

media = (nota1 + nota2) / 2

print('Sua média é ' + str(media))

if media > 7:
    print('Aprovado!')
elif media < 5:
    print('Reprovado')
else:
    print('Recuperação')