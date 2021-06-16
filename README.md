# What this script does

This python script will automatically enroll you to any class saved in your shopping cart in CUNYFirst.
It uses image recognition to identify and click in your browser. And it will check if any course opens up every 5 min and then it will automatically enroll you in those courses.
It stops after it enrolls at least **one** class. So, you will have to run the script again to keep checking for any other class in your shopping cart.


## Initial Setup Requirements:

Step 1:
Make sure these packages are installed:
	1) pyautogui
	2) pillow

To install these package, type in terminal:
pip install pyautogui pillow OR pip3 install pyautogui pillow

Step 2:
Clone this repository in you computer.
<!-- put code in here -->

Step 3:
Put some classes in your shopping cart in CUNYFirst if its empty.

Step 4:
Finally, you need to provide some screenshots of specific areas of the CUNYFirst interface in order for the script to know where it should click. Since every display has different screen resolutions, you will need to provide screenshot samples from the computer you will run this on for it to work.

Put these screenshot samples inside the Samples directory 

![No.1](https://github.com/fake-root/cuny-auto-enroll/blob/main/ScreenShots/1.png)


## To run the script

Open your terminal or command prompt, then goto the directory the python script is located. Open CUNYFirst in a browser. And simply run the script.
python autoEnroll.py OR python3 autoEnroll.py