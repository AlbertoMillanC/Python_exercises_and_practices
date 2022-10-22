# bot whatsapp

import pyautogui as pg
import time 

open('C:\Program Files (x86)\WhatsApp\WhatsApp.exe')
a = txt.readlines()
print(a)
time.sleep(2)
pg.hotkey('win', 'r')
time.sleep(1)
pg.typewrite('chrome')
time.sleep(1)
pg.press('enter')
time.sleep(3)
pg.hotkey('ctrl', 'l')
pg.typewrite('https://web.whatsapp.com/')
pg.press('enter')
time.sleep(15)
for i in a:
    pg.typewrite(i)
    time.sleep(1)
    pg.press('enter')
    time.sleep(1)
    pg.typewrite('hello')
    time.sleep(1)
    pg.press('enter')
    time.sleep(1)



