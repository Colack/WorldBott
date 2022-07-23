# Generate a new status
def statusChange():
    # Move to the Profile button and click it
    pyautogui.moveTo(1050, 745, duration=1)
    pyautogui.click(1050, 745)

    # Move to the edit button and click it.
    pyautogui.moveTo(800, 310, duration = 1)
    pyautogui.click(800, 310)

    # Move to the text box and click it.
    pyautogui.moveTo(1032, 280, duration = 1)
    pyautogui.click(1032, 280)

    # Type "CTRL + A" to select all the text.
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    
    # Type "DELETE" to delete the text.
    pyautogui.keyUp('ctrl')
    pyautogui.press('delete')

    # Update the status to the default status.
    pyautogui.typewrite(default_status)

    # Move to the save button and click it.
    pyautogui.moveTo(1100, 730, duration=1)
    pyautogui.click(1100, 730)
