titulo = 'Completa Ola mundo'
'''
Data: 28/03/2023
Autor: Felipe
Descrição: Ao digitar ola, completa com a palavra mundo
'''
print('Bem vindo ao programa ' + titulo + '\n')

import keyboard
texto = ''

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        if event.name.isalpha() and len(event.name) == 1:
            texto += event.name
        elif event.name == 'backspace':
            texto = texto[:-1]
        print(texto)

        if 'ola' in texto:
            texto = ''
            keyboard.write(' mundo')