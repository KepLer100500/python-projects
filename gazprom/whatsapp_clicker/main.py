from pyautogui import click, typewrite, keyDown, hotkey
from pyautogui import FAILSAFE
from time import sleep
from pyperclip import copy


def send_message():
    sleep(2)
    click(100, 20)        # chrome button
    sleep(5)
    click(300, 120)       # address string
    typewrite('https://web.whatsapp.com/')
    sleep(5)
    keyDown('Enter')      # emulate Enter button
    sleep(23)
    click(300, 330)       # search string
    sleep(3)
    typewrite('twi')      # first simbols searching group
    sleep(5)
    click(300, 450)       # select group
    sleep(3)
    copy('test тест 123') # input text into clipboard
    sleep(3)
    hotkey('ctrl', 'v')   # emulate Ctrl + V
    sleep(3)
    click(1470,850)       # send button
    sleep(2)
    click(1586,50)        # esc button
    sleep(2)
    click(1137,489)       # accept button
    sleep(2)

def main():
    FAILSAFE = False
    send_message()

if __name__ == '__main__':
    main()