import time
import pyautogui
x = 10
y = 10
while True:
    x =  0 - x
    y = 0 - y
    pyautogui.move( x, y , duration=0.1)
    time.sleep(10)