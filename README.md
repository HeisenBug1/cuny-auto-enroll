
# What this script does

This **python** script will automatically enroll you to any class saved in your shopping cart in CUNYFirst.
It uses image recognition to identify and click in your browser. And it will check if any course opens up every 5 min and then it will automatically enroll you in those courses.
It stops after it enrolls at least **one** class. So, you will have to run the script again to keep checking for any other class in your shopping cart.


## Initial Setup Requirements:

Step 0:
Make sure the latest python is installed.

Step 1:
Make sure these python packages are installed:

 1. `pyautogui`
 2. `pillow`

To install these package, type in terminal:
`pip install pyautogui pillow` OR `pip3 install pyautogui pillow`

Step 2:
Clone this repository in you computer. Type in terminal:
`git clone https://github.com/rez1-inf/cuny-auto-enroll.git`

Step 3:
Put some classes in your shopping cart in CUNYFirst if its empty.

Step 4:
Finally, you need to provide some screenshots of specific areas of the CUNYFirst interface in order for the script to know where it should click. Since every display has different screen resolutions, you will need to provide screenshot samples from the computer you will run this on for it to work.

Put these screenshot samples inside the **Samples** directory
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
