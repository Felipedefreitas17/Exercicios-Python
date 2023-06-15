titulo = 'Digimon'
'''
Data: 23/03/2023
Autor: Felipe
Descrição: Tranforma o nome em digimon
'''
print('Bem vindo ao programa ' + titulo + '\n')

def digimon(_nome):
    try:
        _nome = _nome[:4] + 'mon'
        return _nome
    except:
        return "Erro na função digimon"

#print('Digite seu nome')
#nome = input()

digimon_1 = digimon("Anderson")
digimon_2 = digimon("Joana")
digimon_3 = digimon("Pedro")
print(digimon_1)
print(digimon_2)
print(digimon_3)
print(digimon(10))
