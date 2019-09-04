from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

print('you have got 5 seconds to focus your input text space')
time.sleep(5)

f= open("rutas.txt","r")

contents =f.read()

keyboard.type(contents)