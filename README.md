
# What this script does

This **python** script will automatically enroll you to any course saved in your shopping cart in CUNYFirst.
It uses image recognition to identify and click in your browser. And it will check if any course opens up every 5 min and then it will automatically enroll you in those courses.
It stops after enrolling **at least one** course. So, you will have to run the script again to keep checking for any other classes in your shopping cart.


## Initial Setup Requirements:

**Step 0:**
Make sure the latest python is installed in your computer.

**Step 1:**
Make sure these python packages are installed:

 1. Windows: run in command prompt `pip install pyautogui pillow`
 2. MAC: run in terminal `sudo pip3 install pyobjc-framework-Quartz pyobjc-core pyobjc pyautogui pillow`
 3. Linux: run in terminal `sudo pip3 install python3-xlib pyautogui pillow`
 
 Linux needs additional dependencies: `sudo apt install scrot python3-tk python3-dev`

**Step 2:**
Clone this repository in you computer. Type in terminal:

`git clone https://github.com/rez1-inf/cuny-auto-enroll.git`

**Step 3:**
Put some classes in your shopping cart in CUNYFirst if its empty.

**Step 4:**
Finally, you need to provide some screenshots of specific areas of the CUNYFirst interface in order for the script to know where it should click. Since every display has different screen resolutions, you will need to provide screenshot samples from the computer you will run this on for it to work.

Take screenshots of the **red boxes** displayed below, and store them inside the **Samples** directory and name them as `01.png, 02.png ...` or `01.jpg, 02.jpg...` as listed below. Note: png is better since it's lossless, hence it contains accurate color code for each pixel. It might work with jpg, I'm not sure, I didnt test with jpg.

For reference, view the ones I used in my computer inside the samples directory. You can try to see if my samples work for you, but most likely you will need to provide your own. If you do provide your own, make sure to remove/replace mine. Since, there cannot be more or less than 11 sample files inside that directory.

![No.1](https://github.com/rez1-inf/cuny-auto-enroll/blob/main/Required%20Screen%20Shots/1.png)
![No.2](https://github.com/rez1-inf/cuny-auto-enroll/blob/main/Required%20Screen%20Shots/2.png)
![No.3](https://github.com/rez1-inf/cuny-auto-enroll/blob/main/Required%20Screen%20Shots/3.png)
![No.4](https://github.com/rez1-inf/cuny-auto-enroll/blob/main/Required%20Screen%20Shots/4.png)
![No.5](https://github.com/rez1-inf/cuny-auto-enroll/blob/main/Required%20Screen%20Shots/5.png)
![No.6](https://github.com/rez1-inf/cuny-auto-enroll/blob/main/Required%20Screen%20Shots/6.png)
![No.7](https://github.com/rez1-inf/cuny-auto-enroll/blob/main/Required%20Screen%20Shots/7.png)

## To run the script

Open your terminal, then goto the directory the python script is located. Open CUNYFirst in a browser. And simply run the script.
`python autoEnroll.py` OR `python3 autoEnroll.py`

*Note*: This script assumes your browser automatically fills in login information for CUNYFirst

Please let me know if you face any issues. I'll try my best to fix them.
