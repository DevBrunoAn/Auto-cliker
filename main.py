from os import truncate, write
from typing import Container
from pynput import keyboard
from pynput.mouse import Button, Controller
import keyboard

while True:
    mouse = Controller()

    inicia = False
    contador = 0

    while contador == 0:

        if inicia == False:
            if keyboard.is_pressed('o'):
                inicia = True

        if inicia == True:
            while inicia == True:
                mouse.click(Button.left, 2)
                # time.sleep(0.01)
                if keyboard.is_pressed('p'):
                    inicia = False
                    print('Desligou')

        if keyboard.is_pressed('i'):
            contador += 1
            print('Fechou')
            exit()
