titulo = 'Validação CPF'
'''
Data: 21/03/2023
Autor: Felipe
Descrição: Valida o CPF
'''
print('Bem vindo ao programa ' + titulo + '\n')

print('Por favor, digite o cpf')
cpf = input('CPF: ')

if '.' and '-' in cpf:
    lista_cpf_1 = cpf.split('.')
    lista_cpf_2 = lista_cpf_1[2].split('-')
    print(cpf)
    print(lista_cpf_1)
    print(lista_cpf_2)
    cpf_2 = ''
    for indice, digitos in enumerate(lista_cpf_1):
        if indice < 2:
            cpf_2 += digitos
    print(cpf_2)
    for indice, digitos in enumerate(lista_cpf_2):
        if indice < 2:
            cpf_2 += digitos
    print(cpf_2)
    cpf = cpf_2
lista_cpf = list(cpf)

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
    print('1º digito do CPF Válido')
    resultado = 0
    for indice, valor in enumerate(lista_cpf):
        if indice <= 9:
            indice_lista = 11 - indice
            mult = int(valor) * indice_lista
            print(indice_lista, 'x', valor, '=', mult)
            resultado += mult
    print('Soma:', resultado)

    resultado = resultado * 10
    print('Soma x 10 =', resultado)

    resultado = resultado % 11

    print('Resto da divisão por 11 =', resultado)

    if resultado > 9:
        resultado = 0

    print('Resultado:', resultado, 'tipo:', type(resultado))
    print('Digito verificador:', cpf[10], 'tipo:', type(cpf[10]))

    if resultado == int(cpf[10]):
        print('2º digito do CPF Válido')

    else:
        print('CPF Inválido')
else:
    print('CPF Inválido')
