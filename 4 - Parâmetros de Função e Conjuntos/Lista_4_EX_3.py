titulo = 'Validação CPF 1º Digito'
'''
Data: 21/03/2023
Autor: Felipe
Descrição: Valida o primeiro digito verificador do CPF
'''
print('Bem vindo ao programa ' + titulo + '\n')

print('Por favor, digite o cpf (somente números)')
cpf = input('CPF: ')

lista_cpf = list(cpf)
print(cpf)
print(lista_cpf)
resultado = 0
for indice, valor in enumerate(lista_cpf):
    if indice <= 8:
        indice_lista = 10 - indice
        mult = int(valor) * indice_lista
        print(indice_lista, 'x', valor, '=', mult)
        resultado += mult
print('Soma:',resultado)

resultado = resultado * 10
print('Soma x 10 =',resultado)

resultado = resultado % 11

print('Resto da divisão por 11 =', resultado)

if resultado > 9:
    resultado = 0

print('Resultado:', resultado, 'tipo:',type(resultado))
print('Digito verificador:',cpf[9],'tipo:',type(cpf[9]))

if resultado == int(cpf[9]):
    print('CPF Válido')
else:
    print('CPF Inválido')