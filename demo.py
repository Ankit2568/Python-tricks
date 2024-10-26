import time
import pyautogui

pyautogui.hotkey('win','2')
time.sleep(1)
pyautogui.hotkey('ctrl','f')
pyautogui.hotkey('ctrl','a')
pyautogui.keyDown('backspace')
pyautogui.write('Any contack name')
pyautogui.press("down")
pyautogui.press("enter")
for _ in range(300):
    pyautogui.write('Hello world')
    pyautogui.press("enter")
    time.sleep(0.5)
   
