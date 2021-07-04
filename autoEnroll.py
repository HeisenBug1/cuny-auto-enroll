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
OS_Info = platform.system()

# check screen resolution and set sample directory
x, y = pyautogui.size()
samplesDir += str(x) +"x"+ str(y) +"/"

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
            print("Please make sure there are no hidden and/or unusable files in that directory. Quitting")
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
def getSample(sampleNum):
    return (samplesDir + samples[sampleNum-1])

# click based on
def click(sampleNum):
    x, y = pyautogui.locateCenterOnScreen(getSample(sampleNum), confidence=0.9)
    if coordinates is not None:
        if OS_Info == "Darwin":
            pyautogui.click(x/2, y/2)
        else:
            pyautogui.click(x, y)
        return True
    else:
        return False

# choose a term
def takeTermInput(coordinates):
    num = input("Enter a number from 1 - "+str(len(coordinates))+": ")
    num = int(num)
    if num > 0 and num <= len(coordinates):
        return (num -1)
    else:
        takeTermInput()

# relogin if something goes wrong and try again
def re_login():
    coordinates = pyautogui.locateOnScreen(getSample(2))
    if coordinates is not None:
        pyautogui.click(coordinates)
    else:
        print("Can't locate browser for CUNY. Quitting")
        print("Please replace sample for: " + getSample(2) +"\n")
        sys.exit(3)
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(0.5)
    pyautogui.typewrite("home.cunyfirst.cuny.edu")
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(5)

# logs in to CUNYFirst from start page
def initialLogin():
    coordinates = pyautogui.locateOnScreen(getSample(1))
    if coordinates is not None:
        pyautogui.click(coordinates)
        time.sleep(5)
        return True
    else:
        print("Can't find initial login button")
        print("If it keeps happening, please replace sample for: " + getSample(1) +"\n")
        return False

# goto student center 
def gotoStudentCenter():
    coordinates = pyautogui.locateOnScreen(getSample(3))
    if coordinates is not None:
        pyautogui.click(coordinates)
        time.sleep(5)
        return True
    else:
        print("Can't find Student Center")
        print("If it keeps happening, please replace sample for: " + getSample(3) +"\n")
        return False

# goto plan in student center
def gotoPlan():
    coordinates = pyautogui.locateOnScreen(getSample(4))
    if coordinates is not None:
        pyautogui.click(coordinates)
        time.sleep(5)
        return True
    else:
        print("Can't find cart in student center")
        print("If it keeps happening, please replace sample for: " + getSample(4) +"\n")
        return False

# clicks the shopping cart
def clickCart():
    coordinates = pyautogui.locateOnScreen(getSample(5))
    if coordinates is not None:
        pyautogui.click(coordinates)
        time.sleep(5)
        return True
    else:
        print("Can't find Shopping Cart")
        print("If it keeps happening, please replace sample for: " + getSample(5) +"\n")
        return False

# click a term
def clickTerm():
    global term
    global termSet
    if termSet:
        coordinates = list(pyautogui.locateAllOnScreen(getSample(6)))
        if coordinates is not None and len(coordinates) >= 1:
            pyautogui.click(coordinates[term])
            time.sleep(1)
            return True
        else:
            print("Expected term selection page but can't find. Trying to re-login (reset)")
            return False
    else:
        coordinates = list(pyautogui.locateAllOnScreen(getSample(6)))
        if coordinates is not None and len(coordinates) >= 1:
            print("There are " + str(len(coordinates)) +" terms on the screen")
            print("Please select one")
            term = takeTermInput(coordinates)
            pyautogui.click(coordinates[term])
            termSet = True
            time.sleep(1)
            return True
        else:
            print("Expected term selection page but can't find. Trying to re-login (reset)")
            print("If it keeps happening, please replace sample for: " + getSample(6) +"\n")
            return False

# clicks continue after selecting a term
def clickContinue():
    coordinates = pyautogui.locateOnScreen(getSample(7))
    if coordinates is not None:
        pyautogui.click(coordinates)
        time.sleep(5)
        return True
    else:
        print("Can't find continue button")
        print("If it keeps happening, please replace sample for: " + getSample(7) +"\n")
        return False

# click a single check box for 1 open class (this is used in a loop from caller)
def clickCheckBox(checkBoxes, openClass):
    minDiff = 999999999
    index = -1
    count = 0
    y2 = openClass[1]
    for box in checkBoxes:
        y1 = box[1]
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
            if count % 10 == 0:
                print("Note: if you can observe an open class and this script is not noticing it,\nthen please replace sample for: " + getSample(11) +"\n")
            time.sleep(sleepTime)
        else:
            checkBoxes = list(pyautogui.locateAllOnScreen(getSample(8)))
            if len(checkBoxes) < len(gLight):
                print("# of check boxes are less than open classes. Re-Trying")
                print("If it keeps happening, please replace sample for: " + getSample(8) +"\n")
                loggedIn = False
                break

            print("Found: " + str(len(gLight)) +" classes open")

            # select all available classes
            for openClass in gLight:
                clickCheckBox(checkBoxes, openClass)
            
            time.sleep(1)

            # finish enrolling in open classes
            enroll = pyautogui.locateOnScreen(getSample(9))
            if enroll is None:
                print("Can't find enroll button")
                print("If it keeps happening, please replace sample for: " + getSample(9) +"\n")
                loggedIn = False
                break
            pyautogui.click(enroll)
            time.sleep(5)

            fEnroll = pyautogui.locateOnScreen(getSample(10))
            if fEnroll is None:
                print("Can't find Finish Enroll button")
                print("If it keeps happening, please replace sample for: " + getSample(10) +"\n")
                loggedIn = False
                continue
            pyautogui.click(fEnroll)
            print("Enrolled [" + datetime.now().strftime("%h %d - %I:%M %p") + "]")
            enrolled = True
            break

        if clickCart() == False:
            loggedIn = False
            break;
