titulo = 'Criador de Macro Mouse'
'''
Data: 29/03/2023
Autor: Felipe
Descrição: Ao clicar CRTL, inica a gravação de uma macro de mouse, ao clicar CRTL novamente
salva o arquivo em CSV
'''
print('Bem vindo ao programa ' + titulo + '\n')

import time
import csv
import mouse
import keyboard

path = 'Mouse Tracker/macro.csv'

ctrl_pressionado = False
gravando = False
mouse_events = []


while True:
    if keyboard.is_pressed('ctrl'):
        if not gravando:
            gravando = True
            print("Começando a gravar...")
            time.sleep(0.5)
        else:
            gravando = False
            print("Parando de gravar...")
            break

    if gravando:
        evento = []
        if mouse.is_pressed('left'):
            evento.append('move')
            pos_mouse = mouse.get_position()
            evento.append(pos_mouse[0])
            evento.append(pos_mouse[1])
            mouse_events.append(evento)
            evento = ['click']
            evento.append('left')
            mouse_events.append(evento)
            time.sleep(0.1)
        elif mouse.is_pressed('right'):
            evento.append('move')
            pos_mouse = mouse.get_position()
            evento.append(pos_mouse[0])
            evento.append(pos_mouse[1])
            mouse_events.append(evento)
            evento = ['click']
            evento.append('right')
            mouse_events.append(evento)
            time.sleep(0.1)
        elif mouse.is_pressed('middle'):
            evento.append('move')
            pos_mouse = mouse.get_position()
            evento.append(pos_mouse[0])
            evento.append(pos_mouse[1])
            mouse_events.append(evento)
            evento = ['click']
            evento.append('middle')
            mouse_events.append(evento)
            time.sleep(0.1)


if len(mouse_events) > 0:
    with open(path,'w',newline='') as file:
        writer = csv.writer(file)
        for row in mouse_events:
            writer.writerow(row)