titulo = 'Inversor de texto'
'''
Data: 23/03/2023
Autor: Felipe
Descrição: Inverte um texto
'''
print('Bem vindo ao programa ' + titulo + '\n')

def inversor_de_texto(_texto):
    texto_invertido = ''
    for indice, letra in enumerate(_texto):
        texto_invertido += _texto[-indice - 1]
    return texto_invertido

while True:
    print(inversor_de_texto(input('Digite um texto: ')))

