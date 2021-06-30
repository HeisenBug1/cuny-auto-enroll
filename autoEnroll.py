from platform import release
from datetime import datetime
import platform
import pyautogui
import time
import sys
import os.path
from os import listdir
import os

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = False

count = 0
sleepTime = 300
enrolled = False
loggedIn = False
samplesDir = 'Samples/'
samples = None
termSet = False
term = None

# check screen resolution and set sample directory
x, y = pyautogui.size()
if x == 1440 and y == 900:
    samplesDir += "1440x900/"
if x == 1920 and y == 1080:
    samplesDir += "1920x1080/"

# Create samples directory for current screen resolution if it doesn't exist
if os.path.exists(samplesDir) is False:
    os.mkdir(samplesDir)
    print("Please put the samples in " + samplesDir + " directory and then re-run this script")
    sys.exit(0)

# check if all the files exist in the Samples directory
while True:
    tryAgain = False
    if len(listdir(samplesDir)) != 11:
        if platform.system() == 'Darwin':
            if os.path.exists(samplesDir + ".DS_Store"):
                os.remove(samplesDir + ".DS_Store")
                tryAgain = True
        if not tryAgain:
            print("There needs to be EXACTLY 11 sample screenshots inside the " + samplesDir +" directory.")
            print("Please make sure there are no hidden or unusable files in that directory. Quitting")
            sys.exit(1)
    else:
        samples = listdir(samplesDir)
        samples.sort()
        for i in range(0, 9):
            if samples[i][0] != "0":
                print("First 9 files need to start with \"0\"")
                print("eg: 05.png... Please rename.. Quitting")
                sys.exit(2)
        break

# get a sample file location
def getSample(index):
    return (samplesDir + samples[index-1])

# choose a term
def takeTermInput(cordinates):
    num = input("Enter a number from 1 - "+str(len(cordinates))+": ")
    num = int(num)
    if num > 0 and num <= len(cordinates):
        return (num -1)
    else:
        takeTermInput()

# relogin if something goes wrong and try again
def re_login():
    cordinates = pyautogui.locateOnScreen(getSample(2))
    if cordinates is not None:
        pyautogui.click(cordinates)
    else:
        print("Can't locate browser for CUNY. Quitting")
        sys.exit(3)
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(0.5)
    pyautogui.typewrite("home.cunyfirst.cuny.edu")
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(5)

# logs in to CUNYFirst from start page
def initialLogin():
    cordinates = pyautogui.locateOnScreen(getSample(1))
    if cordinates is not None:
        pyautogui.click(cordinates)
        time.sleep(5)
        return True
    else:
        print("Can't find initial login button")
        return False

# goto student center 
def gotoStudentCenter():
    cordinates = pyautogui.locateOnScreen(getSample(3))
    if cordinates is not None:
        pyautogui.click(cordinates)
        time.sleep(5)
        return True
    else:
        print("Can't find Student Center")
        return False

# goto plan in student center
def gotoPlan():
    cordinates = pyautogui.locateOnScreen(getSample(4))
    if cordinates is not None:
        pyautogui.click(cordinates)
        time.sleep(5)
        return True
    else:
        print("Can't find cart in student center")
        return False

# clicks the shopping cart
def clickCart():
    cordinates = pyautogui.locateOnScreen(getSample(5))
    if cordinates is not None:
        pyautogui.click(cordinates)
        time.sleep(5)
        return True
    else:
        print("Can't find Shopping Cart")
        return False

# click a term
def clickTerm():
    global term
    global termSet
    if termSet:
        cordinates = list(pyautogui.locateAllOnScreen(getSample(6)))
        if cordinates is not None and len(cordinates) >= term:
            pyautogui.click(cordinates[term])
            time.sleep(1)
            return True
        else:
            print("Expected term selection page but can't find. Trying to re-login (reset)")
            return False
    else:
        cordinates = list(pyautogui.locateAllOnScreen(getSample(6)))
        if cordinates is not None:

            print("There are " + str(len(cordinates)) +" terms on the screen")
            print("Please select one")
            term = takeTermInput(cordinates)
            pyautogui.click(cordinates[term])
            termSet = True
            time.sleep(1)
            return True
        else:
            print("Can't find Summer Term")
            return False

# clicks continue after selecting a term
def clickContinue():
    cordinates = pyautogui.locateOnScreen(getSample(7))
    if cordinates is not None:
        pyautogui.click(cordinates)
        time.sleep(5)
        return True
    else:
        print("Can't find continue button")
        return False

# click check boxes for open classes
def clickCheckBox(checkBoxes, openClass):
    minDiff = 999999999
    index = -1
    count = 0
    y2 = openClass[1]
    for checks in checkBoxes:
        y1 = checks[1]
        diff = abs(y2 - y1)
        if minDiff > diff:
            minDiff = diff
            index = count
        count += 1
    pyautogui.click(checkBoxes[index])


while enrolled == False:
    one = initialLogin()
    two = gotoStudentCenter()
    three = gotoPlan()
    if one == False and two == False and three == False:
        re_login()
    else:
        loggedIn = True

    while loggedIn == True and enrolled == False:
        if clickTerm() == False:
            loggedIn = False
            break
        if clickContinue() == False:
            loggedIn = False
            break

        gLight = list(pyautogui.locateAllOnScreen(getSample(11)))
        if len(gLight) == 0:    # if no class is open
            count = count + 1
            print("Try Count: " + str(count) + " (wait " + str(sleepTime/60) +" min) [" + datetime.now().strftime("%h %d - %I:%M %p") + "]")
            time.sleep(sleepTime)
        else:
            checkBoxes = list(pyautogui.locateAllOnScreen(getSample(8)))

            print("Found: " + str(len(gLight)) +" classes open")

            # select all available classes
            for i in range(0, len(gLight)):
                pyautogui.click(189, gLight[i][1]+5, button='left')
                time.sleep(1)

            # finish enrolling in open classes
            enroll = pyautogui.locateOnScreen(getSample(9))
            if enroll is None:
                print("Can't find enroll button")
                loggedIn = False
                break
            pyautogui.click(enroll)
            time.sleep(5)

            fEnroll = pyautogui.locateOnScreen(getSample(10))
            if fEnroll is None:
                print("Can't find Finish Enroll button")
                loggedIn = False
                continue
            pyautogui.click(fEnroll)
            print("Enrolled [" + datetime.now().strftime("%h %d - %I:%M %p") + "]")
            enrolled = True
            break

        if clickCart() == False:
            loggedIn = False
            break;
