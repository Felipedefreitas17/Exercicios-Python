titulo = 'Desenhar Letra do Nome'
'''
Data: 28/03/2023
Autor: Felipe
Descrição: Ao teclar CTRL desenha a primeira letra do seu nome (D)
'''
print('Bem vindo ao programa ' + titulo + '\n')

import keyboard
import mouse

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == 'ctrl':
            mouse.drag(0, 0, 0, 200, absolute=False, duration=0.3)
            mouse.drag(0, 0, 100, -50, absolute=False, duration=0.1)
            mouse.drag(0, 0, 25, -50, absolute=False, duration=0.1)
            mouse.drag(0, 0, -25, -50, absolute=False, duration=0.1)
            mouse.drag(0, 0, -100, -50, absolute=False, duration=0.1)

