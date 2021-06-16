from platform import release
import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = False

count = 0
sleepTime = 300
enrolled = False
loggedIn = False
cordinates = None

def takeTermInput():
    num = input("Enter a number from 1 - "+str(len(cordinates))+": ")
    num = int(num)
    if num > 0 and num <= len(cordinates):
        return (num -1)
    else:
        takeTermInput()

def re_login():
    cordinates = pyautogui.locateOnScreen('cunyFirst.png')
    if cordinates is not None:
        pyautogui.click(cordinates)
    else:
        print("Can't locate browser for CUNY. Quitting")
        quit()
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(0.5)
    pyautogui.typewrite("home.cunyfirst.cuny.edu")
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(5)

def initialLogin():
    cordinates = pyautogui.locateOnScreen('login.png')
    if cordinates is not None:
        pyautogui.click(cordinates)
        time.sleep(5)
        return True
    else:
        print("Can't find initial login button")
        return False

def gotoStudentCenter():
    cordinates = pyautogui.locateOnScreen('stuCent.png')
    if cordinates is not None:
        pyautogui.click(cordinates)
        time.sleep(5)
        return True
    else:
        print("Can't find Student Center")
        return False

def goto_cart_in_stuCenter():
    cordinates = pyautogui.locateOnScreen('eShopCart.png')
    if cordinates is not None:
        pyautogui.click(cordinates)
        time.sleep(5)
        return True
    else:
        print("Can't find cart in student center")
        return False

def isSignedIn():
    if pyautogui.locateOnScreen('signedIn.png') is not None:
        return True
    else:
        return False

def clickCart():
    cordinates = pyautogui.locateOnScreen('cart.png')
    if cordinates is not None:
        pyautogui.click(cordinates)
        time.sleep(5)
        return True
    else:
        print("Can't find Shopping Cart")
        return False

def clickSummerTerm():
    cordinates = pyautogui.locateOnScreen('summer.png')
    if cordinates is not None:
        pyautogui.click(cordinates[0]+6, cordinates[1]+6)
        time.sleep(1)
        return True
    else:
        print("Can't find Summer Term")
        return False

def clickContinue():
    cordinates = pyautogui.locateOnScreen('cont.png')
    if cordinates is not None:
        pyautogui.click(cordinates)
        time.sleep(5)
        return True
    else:
        print("Can't find continue button")
        return False

while enrolled == False:
    if initialLogin() == False and gotoStudentCenter() == False and goto_cart_in_stuCenter() == False:
        re_login()
    else:
        loggedIn = True

    while loggedIn == True and enrolled == False:
        if clickSummerTerm() == False or clickContinue() == False:
            loggedIn = False
            break

        gLight = list(pyautogui.locateAllOnScreen('green.png'))
        if len(gLight) == 0:    # if no class is open
            count = count + 1
            print("Try Count: " + str(count) + " (wait " + str(sleepTime/60) +" min)")
            time.sleep(sleepTime)
        else:
            print("Found: " + str(len(gLight)) +" classes open")

            # select all available classes
            for i in range(0, len(gLight)):
                pyautogui.click(189, gLight[i][1]+5, button='left')
                time.sleep(1)

            # finish enrolling in open classes
            enroll = pyautogui.locateOnScreen('enroll.png')
            if enroll is None:
                print("Can't find enroll button")
                loggedIn = False
                break
            pyautogui.click(enroll)
            time.sleep(5)

            fEnroll = pyautogui.locateOnScreen('fEnroll.png')
            if fEnroll is None:
                print("Can't find Finish Enroll button")
                loggedIn = False
                continue
            pyautogui.click(fEnroll)
            print("Enrolled")
            enrolled = True
            break

        if clickCart() == False:
            loggedIn = False
            break;
