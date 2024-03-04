import time
import traceback

import pyautogui

while True:
    try:
        time.sleep(1)
        pyautogui.click(pyautogui.locateCenterOnScreen('close.png'))
        pyautogui.click(pyautogui.locateCenterOnScreen('close2.png'))
    except:
        print(traceback.format_exc())
        time.sleep(5)
        pass