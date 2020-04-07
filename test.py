import pyautogui
import time
import pyperclip
import datetime

def click():
    """
    crontab -e

    DISPLAY=:1.0
    XAUTHORITY=/home/pi/.Xauthority
    PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games
    30 8 * * * python3 /home/pi/morning_clicker.py
    """
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

pyautogui.FAILSAFE = False
click()
