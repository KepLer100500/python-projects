import pyautogui
import time
import pyperclip
import datetime

def click():
    time.sleep(2)
    pyautogui.click(100, 20)   # chrome button
    time.sleep(5)
    pyautogui.click(300, 120)    # address string
    pyautogui.typewrite('https://web.whatsapp.com/')
    time.sleep(5)
    pyautogui.keyDown('Enter')  # emulate Enter button
    time.sleep(23)
    pyautogui.click(300, 330)   # search string
    time.sleep(3)
    pyautogui.typewrite('twi')  # first simbols searching group
    time.sleep(5)
    pyautogui.click(300, 450)   # select group
    time.sleep(3)
    pyperclip.copy('test тест 123')   # input text into clipboard
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'v')   # emulate Ctrl + V
    time.sleep(3)
    pyautogui.click(1470,850)  # send button
    time.sleep(2)
    pyautogui.click(1586,50)  # esc button
    time.sleep(2)
    pyautogui.click(1137,489) # accept button
    time.sleep(2)
    a = datetime.datetime.today()
    print(a.day,'-',a.month,'-',a.year,' ',a.hour, ':',a.minute, ':',a.second,sep='')  # success printing time
    return 1

pyautogui.FAILSAFE = False
flag = 0
while(1):
    a = datetime.datetime.today()
    if(a.hour == 8 and a.minute == 30 and flag == 0):
        flag = click()
    elif(a.hour == 8 and a.minute == 31 and flag == 1):
        flag = 0
    time.sleep(1)
