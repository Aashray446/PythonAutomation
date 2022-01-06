import pyperclip
import pyautogui
import time
##pyautogui.displayMousePosition()
pyautogui.moveTo(1500,240)
time.sleep(10)
pyautogui.click()
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')

print(pyperclip.paste())