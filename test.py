import pyautogui
import time
import pyperclip

#pyautogui.click(25, 1060)   # win button
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
pyautogui.typewrite('shaik')
time.sleep(3)
pyautogui.click(300, 450)   # select group
time.sleep(3)
pyperclip.copy('test тест ололо 123')   # input text into clipboard
time.sleep(3)
pyautogui.hotkey('ctrl', 'v')   # emulate Ctrl + V
time.sleep(3)
pyautogui.click(1470,850)  # send button
