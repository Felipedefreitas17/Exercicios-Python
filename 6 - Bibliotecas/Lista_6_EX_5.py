titulo = 'Macro Teclado'
'''
Data: 29/03/2023
Autor: Felipe
Descrição: Ative uma macro de teclado ao clicar o botão do meio do mouse
'''
print('Bem vindo ao programa ' + titulo + '\n')

import mouse
import keyboard
import time

while True:
    if mouse.is_pressed('middle'):
        keyboard.press_and_release('w')
        time.sleep(0.1)
        keyboard.press_and_release('a')
        time.sleep(0.1)
        keyboard.press_and_release('s')
        time.sleep(0.1)
        keyboard.press_and_release('d')
        time.sleep(0.1)
        keyboard.press_and_release('space')
        time.sleep(0.1)