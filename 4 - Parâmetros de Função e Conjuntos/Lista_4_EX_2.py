titulo = 'Lista de Compras'
'''
Data: 20/03/2023
Autor: Felipe
Descrição: Programa para manipular uma lista de compras
'''
print('Bem vindo ao programa ' + titulo + '\n')

lista_de_compras = []
while True:
    print('''Digite (I) para incluir um item na lista,
Digite (D) para deletar um item da lista,
Digite (L) para listar os valores ou 
Digite (X) para encerrar o programa.''')

    escolha = input().upper()


    while escolha == 'I':
        print('Digite um Item para incluir ou (Q) para voltar')
        item = input('Item: ').upper()
        if item == 'Q':
            break
        else:
            if item in lista_de_compras:
                print('Item já cadastrado')
            else:
                lista_de_compras.append(item)
    if escolha == 'X':
        print('Encerrando o programa')
        break
    elif escolha == 'D':
        for indice, valor in enumerate(lista_de_compras,start=1):
            print(indice,'-',valor)
        item = int(input('Indice do Item a ser deletado: '))
        deletado = lista_de_compras.pop(item-1)
        print('\nO item',deletado,'foi deletado\n')
    elif escolha == 'L':
        print('Lista de Compras')
        for indice, valor in enumerate(lista_de_compras,start=1):
            print(indice,'-',valor)
    else:
        print('Você digitou um comando incorreto')