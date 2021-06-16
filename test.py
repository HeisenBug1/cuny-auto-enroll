import pyautogui
import time
from os import listdir

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = False

count = 0

# print(listdir())
# pyautogui.click(list(pyautogui.locateAllOnScreen('Samples/6.png'))[0])
print(list(pyautogui.locateAllOnScreen('Samples/6.png')))