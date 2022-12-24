import pyautogui
import time
time.sleep(1)
for i in range(100):
    pyautogui.typewrite("i love yo man :)" + str(i))
    pyautogui.press("enter")
