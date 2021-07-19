from os import truncate, write
from typing import Container
from pynput import keyboard
from pynput.mouse import Button, Controller
import keyboard
import time
import csv

mouse = Controller()

inicia = False
contador = 0

inicia_key = input("Digite a tecla para iniciar o cliker: ")
desligar_key = input("Digite a tecla para desligar o cliker: ")
sair_key = input("Digite a tecla para sair do auto cliker: ")

while contador == 0:

    if inicia == False:
        if keyboard.is_pressed(inicia_key):
            inicia = True

    if inicia == True:
        while inicia == True:
            mouse.click(Button.left, 2)
            # time.sleep(0.01)
            if keyboard.is_pressed(desligar_key):
                inicia = False
                print('Desligou')

    if keyboard.is_pressed(sair_key):
        contador += 1
        print('Fechou')
        exit()