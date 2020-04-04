import pyautogui
import time
import pyperclip

pyautogui.click(25, 1060)   # win button
time.sleep(2)
pyautogui.click(590, 850)   # chrome button
time.sleep(2)
pyautogui.click(500, 50)    # address string
pyautogui.typewrite('https://web.whatsapp.com/')
time.sleep(2)
pyautogui.keyDown('Enter')  # emulate Enter button
time.sleep(20)
pyautogui.click(500, 300)   # search string
time.sleep(2)
pyautogui.typewrite('shaik')
time.sleep(2)
pyautogui.click(500, 420)   # select group
time.sleep(2)
pyperclip.copy('test тест ололо 123')   # input text into clipboard
time.sleep(2)
pyautogui.hotkey('ctrl', 'v')   # emulate Ctrl + V
time.sleep(2)
#pyautogui.click(1625,990)  # send button
