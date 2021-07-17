from os import truncate
from typing import Container
from pynput import keyboard
from pynput.mouse import Button, Controller
import keyboard
import time

mouse = Controller()

inicia = False
contador = 0

while contador == 0:

    if inicia == False:
        if keyboard.is_pressed("q"):
            inicia = True
    
    if inicia == True:
        while inicia == True:
            mouse.click(Button.left, 1)
            time.sleep(0.1)
            if keyboard.is_pressed("p"):
                inicia = False
    
    if keyboard.is_pressed("u"):
            contador += 1
            exit()

    
            



