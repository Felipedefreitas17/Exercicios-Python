titulo = 'Executar Macro Mouse'
'''
Data: 29/03/2023
Autor: Felipe
Descrição: Ao clicar CTRL, executa a macro salva no exercicio LISTA_6_EX_6
'''
print('Bem vindo ao programa ' + titulo + '\n')

import mouse
import keyboard
import csv

path = 'Mouse Tracker/macro.csv'

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == 'ctrl':
            try:
                with open(path,'r') as file:
                    reader = csv.reader(file)
                    for linha in reader:
                        if linha[0] == 'move':
                            mouse.move(linha[1],linha[2],duration=0.3)
                        elif linha[0] == 'click':
                            mouse.click(linha[1])
            except:
                print('Erro ao abrir ou executar arquivo')
