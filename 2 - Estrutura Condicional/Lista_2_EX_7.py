titulo = 'Data  Valida'
'''
Data: 07/03/2023
Autor: Felipe
Descrição: Verifica se uma data é valida
'''
print('Bem vindo ao programa ' + titulo)

print('Por favor, informe um dia')
dia = int(input())

print('Informe um mês')
mes = int(input())

print('Informe um ano')
ano = int(input())

#Verificador se é ano bissexto
if ano % 4 == 0: # É divisel por quatro?
    if ano % 100 > 0: # Não é divisel por 100?
        ano_bissexto = True
    elif ano % 400 == 0: # É divisel por 4, por 100 e por 400?
        ano_bissexto = True
    else:
        ano_bissexto = False
else:
    ano_bissexto = False

# Logica de valor positivo
if ano > 0 and mes > 0 and dia > 0:
    data_positiva = True
else:
    data_positiva = False

# mes valido dentro valor 12
if mes <= 12:
    mes_valido = True
else:
    mes_valido = False

if data_positiva and mes_valido:
    if (mes == 1 or mes == 3 or mes == 5
    or mes == 7 or mes == 8 or mes == 10
    or mes == 12) and dia <= 31:
        data_invalida = False
    elif (mes == 4 or mes == 6 or mes == 9
    or mes == 11) and dia <= 30:
        data_invalida = False
    elif ano_bissexto and mes == 2 and dia <= 29:
        data_invalida = False
    elif not ano_bissexto and mes == 2 and dia <= 28:
        data_invalida = False
    else:
        data_invalida = True
else:
    data_invalida = True


if data_invalida:
    print('Data inválida')
else:
    print('Data válida')
'''
if dia > 0 and mes > 0 and ano > 0:
    if mes <= 12:
        if (mes == 1 or mes == 3 or mes == 5
        or mes == 7 or mes == 8 or mes == 10
        or mes == 12):
            if dia <= 31:
                print('Data válida')
            else:
                print('Data inválida')
        elif (mes == 4 or mes == 6 or mes == 9
        or mes == 11):
            if dia <= 30:
                print('Data válida')
            else:
                print('Data inválida')
        else: # mes de fevereiro
            if ano % 4 == 0:  # É divisel por quatro?
                if ano % 100 > 0:  # Não é divisel por 100?
                    if dia <= 29:
                        print('Data válida')
                    else:
                        print('Data inválida')
                elif ano % 400 == 0:  # É divisel por 4, por 100 e por 400?
                    if dia <= 29:
                        print('Data válida')
                    else:
                        print('Data inválida')
                else:
                    if dia <= 28:
                        print('Data válida')
                    else:
                        print('Data inválida')
            else:
                if dia <= 28:
                    print('Data válida')
                else:
                    print('Data inválida')
    else:
        print('Data inválida')
else:
    print('Data inválida')
'''