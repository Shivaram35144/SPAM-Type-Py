#READ!!!
'''OPEN APPLICATION IN ANOTHER WINDOW. RUN CODE AND TYPE THE TEXT AND TIMES.
THEN KEEP MOUSE POINTER AT WHERE TO TYPE THE TEXT'''

import pyautogui
import time

s=pyautogui.prompt("Write the text to be typed here!")
n=pyautogui.prompt("How many times to type it?")

time.sleep(10)
a=tuple(pyautogui.position())

x=a[0]
y=a[1]
pyautogui.click(x,y)

for i in range(int(n)):
    pyautogui.typewrite(s,interval=0)
    pyautogui.typewrite("\n")

