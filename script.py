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