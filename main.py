from os import truncate, write
from typing import Container
from pynput import keyboard
from pynput.mouse import Button, Controller
import keyboard

while True:
    mouse = Controller()

    inicia = False
    contador = 0

    key_inicia = input("Digite a tecla para iniciar o clicker:")
    key_desligar = input("Digite a tecla para desligar o clicker:")
    key_sair = input("Digite a tecla para sair do clicker: ")

    while contador == 0:

        if inicia == False:
            if keyboard.is_pressed(key_inicia):
                inicia = True

        if inicia == True:
            while inicia == True:
                mouse.click(Button.left, 2)
                # time.sleep(0.01)
                if keyboard.is_pressed(key_sair):
                    inicia = False
                    print('Desligou')

        if keyboard.is_pressed(key_desligar):
            contador += 1
            print('Fechou')
            exit()
