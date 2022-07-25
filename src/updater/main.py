from imports import *

def main():
    STATUS = sg.popup_get_text("New Status: ")
    if STATUS == "":
        main()
    else:
        sg.popup_ok("Updating your status to: " + STATUS)
    pyautogui.moveTo(1050, 745, duration = 0.5)
    pyautogui.click(1050, 745)
    time.sleep(0.5)
    pyautogui.moveTo(800, 310, duration = 0.5)
    pyautogui.click(800, 310)
    time.sleep(0.5)
    pyautogui.moveTo(1032, 280, duration = 0.5)
    pyautogui.click(1032, 280)
    time.sleep(0.5)
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    pyautogui.press('delete')
    time.sleep(0.5)
    pyautogui.typewrite(STATUS)
    pyautogui.moveTo(1100, 730, duration = 0.5)
    pyautogui.click(1100, 730)
    time.sleep(0.5)
    main()

main()
