titulo = 'Converte em Número'
'''
Data: 23/03/2023
Autor: Felipe
Descrição: Converte as letras a seguir:
Letra A  4
Letra B  8
Letra E  3
Letra I  1
Letra O  0
Letra T  7
'''
print('Bem vindo ao programa ' + titulo + '\n')

'''
def alterador_de_texto(_texto):
    texto_alterado = _texto.replace('A', '4')
    texto_alterado = texto_alterado.replace('B', '8')
    texto_alterado = texto_alterado.replace('E', '3')
    texto_alterado = texto_alterado.replace('I', '1')
    texto_alterado = texto_alterado.replace('O', '0')
    texto_alterado = texto_alterado.replace('T', '7')
    return texto_alterado

print(alterador_de_texto(input('Digite um texto: ').upper()))
'''

letras_originais = ['A','B','E','I','O','T','S']
letras_alteradas = ['4','8','3','1','0','7','5']

def alterador_de_texto(_texto):
    _texto = _texto.upper()
    texto_alterado = _texto
    #Aula  --> AULA
    for indice_orig, letra_orig in enumerate(letras_originais):
        if letra_orig in _texto:
            texto_alterado = texto_alterado.replace(letra_orig,letras_alteradas[indice_orig])
    return texto_alterado


texto = input('Digite um texto: ')

print(alterador_de_texto(texto))