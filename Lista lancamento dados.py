import random

numero_de_dados = int(input('Digite quantos dados você quer jogar\n'))


possibilidades = (numero_de_dados * 6) - (numero_de_dados-1)

resultados = []
for dado in range(possibilidades):
    resultados.append(0)


print('Digite o numero de vezes para jogar o(s) dado(s)')
vezes = int(input('Número de Vezes: '))


for lancamento in range(vezes):
    soma = 0
    for dado in range(numero_de_dados):
        soma += random.randint(1,6)
    resultados[soma-numero_de_dados] += 1


for indice, dado in enumerate(resultados,start=numero_de_dados):
    print(indice, ': ', dado)