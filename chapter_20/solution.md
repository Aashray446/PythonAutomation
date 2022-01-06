1. How can you trigger PyAutoGUI’s fail-safe to stop a program?
By moving mouse to upper corner of the screen

2. What function returns the current resolution()?
pyautogui.size()

3. What function returns the coordinates for the mouse cursor’s current position?
pyautogui.position()

4. What is the difference between pyautogui.moveTo() and pyautogui.move()?
moveTo() takes the absolute co-ordinates of the screen and .move() moves the cursor relatively

5. What functions can be used to drag the mouse?
pyautogui.drag and pyautogui.dragto()

6. What function call will type out the characters of "Hello, world!"?
pyautogui.typewrite('Hello, world!')

7. How can you do keypresses for special keys such as the keyboard’s left arrow key?
pyautogui.press('left')

8. How can you save the current contents of the screen to an image file named screenshot.png?
pyautogui.screenshot('file_name.extension')

9. What code would set a two-second pause after every PyAutoGUI function call?
pyautogui.PAUSE = 2

10. If you want to automate clicks and keystrokes inside a web browser, should you use PyAutoGUI or Selenium?
Selenium is made for browser stimulation. It will be a lot easier than using PyAutoGui

11. What makes PyAutoGUI error-prone?
Since it is just manuplulating the keyboard and mouse , it doesn't have any idea what is going on screen and just follow the commands written sequentially and that can cause many error if any external influences changes screen or do something , The whole script will go in some other direction

12. How can you find the size of every window on the screen that includes the text Notepad in its title?
pyautogui.getWindowsWithTitle('Notepad')

13. How can you make, say, the Firefox browser active and in front of every other window on the screen?
fire_screen = pyatuogui.getWindowsWithTitle('Firefox')
fire_screen.acitve()