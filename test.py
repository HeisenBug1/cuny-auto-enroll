import pyautogui
import time
from os import listdir

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = False
samplesDir = 'Samples/'
samples = None
cordinates = None
termSet = False
term = None
count = 0

def checkSamples():
	if len(listdir(samplesDir)) != 11:
		print("There needs to be 11 sample screenshots inside the Samples directory. Quitting")
		quit()
	# else:


# def takeTermInput():
# 	num = input("Enter a number from 1 - "+str(len(cordinates))+": ")
# 	num = int(num)
# 	if num > 0 and num <= len(cordinates):
# 		return (num -1)
# 	else:
# 		takeTermInput()

# def clickSummerTerm():
# 	if termSet:
# 		pyautogui.click(term)
# 		time.sleep(1)
# 		return True
# 	else:
#     	cordinates = list(pyautogui.locateOnScreen())
# 	    if cordinates is not None:
# 	    	print("There are " + str(len(cordinates)) +" terms on the screen")
# 	    	print("Please select one")
# 	    	term = cordinates[takeTermInput()]
# 	    	pyautogui.click(term)
# 	    	termSet = True
# 	        time.sleep(1)
# 	        return True
# 	    else:
# 	        print("Can't find Summer Term")
# 	        return False
# takeTermInput()
# num = input("Enter 1 - "+str(5)+": ")
# print(num)

samples = listdir(samplesDir)
samples.sort()
print(samples)
# pyautogui.click(list(pyautogui.locateAllOnScreen('Samples/6.png'))[0])
# print(list(pyautogui.locateAllOnScreen(samples + '6.png')))