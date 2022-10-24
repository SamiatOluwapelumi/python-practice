import pyautogui as pg
import time

print('the program will rn in 20 sec')
time.sleep(20)

for i in range (100):
    pg.write('paddie miee paddie miee')
    time.sleep(0.5)
    pg.press('Enter')