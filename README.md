# Telegram Automated Bulk Messages

It is a python script that sends the Telegram messages automatically from Telegram desktop application. It can be configured to send advertising messages. It read data from an excel sheet and send a configured message to people.

## Demo
* Video clip on youtube of the script execution. https://youtu.be/EHWqx8r0f2M

## Important Note
* If this repository helped you to understand at least something new please give star this repository which motivates me to work further for the similar kinds for projects.

## Prerequisites

In order to run the python script, your system must have the following programs/packages installed and the contact number should be saved in your phone (You can use bulk contact number saving procedure of email). There is a way without saving the contact number but has the limitation to send the attachment.
* Python 3.8: Download it from https://www.python.org/downloads
* Pandas : Run in command prompt **pip install pandas**
* Xlrd : Run in command prompt **pip install xlrd**
* Pyautogui: Run in command prompt pip install pyautogui
* Telegram Desktop App : Download from https://desktop.telegram.org/

## Approach
* First need to clone this respiratory
* User scans Telegram login QR code to log in into the Telegram Desktop application.
* Run python script script.py using py script.py in the terminal
* The script reads a customized message from an excel sheet.
* The script reads rows one by one and searches that username in the Telegram Desktop Application search box if the username found on Telegram then it will send a configured message otherwise It reads next row. 
* Loop executes until and unless all rows complete.

Note: If you wish to send an image or documents instead of text you can write code to add attachment send functionality.

## Legal
* This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by Telegram or any of its affiliates or subsidiaries. This is an independent and unofficial software. Use at your own risk. Commercial use of this code/repo is strictly prohibited.

## Code
```
# Program to send bulk customized messages through Telegram Desktop application
# Author @inforkgodara

import pyautogui
import pandas
import time

excel_data = pandas.read_excel('Recipients data.xlsx', sheet_name='Recipients')

count = 0

time.sleep(3)

for column in excel_data['Username'].tolist():

      pyautogui.press('esc')
      pyautogui.hotkey('ctrl', 'f')
      time.sleep(1)
      pyautogui.write(str(excel_data['Username'][count]));
      pyautogui.press('enter')
      time.sleep(2)
      pyautogui.press('down')
      pyautogui.press('enter')
      pyautogui.write(str(excel_data['Message'][0]));
      pyautogui.press('enter')
      pyautogui.press('esc')
      count = count + 1

print('The script executed successfully.')
```
Note: The script may not work in case if the accessibility of Telegram changed.

Find it on youtube. https://youtu.be/EHWqx8r0f2M
