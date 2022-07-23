# Like and Comment
def like():
    # Click the post
    pyautogui.moveTo(775, 300, duration = 1)
    pyautogui.click(775, 300)

    # Move to the like button and click it.
    pyautogui.moveTo(775, 730, duration = 1)
    pyautogui.click(775, 730)

    # Move to the comment box and click it.
    pyautogui.moveTo(1140, 730, duration=1)
    pyautogui.click(1140, 730)

    # Move to the comment field and type the default comment.
    pyautogui.moveTo(1140, 700, duration = 1)
    pyautogui.click(1140, 700)
    pyautogui.typewrite(default_comment)

    # Type "ENTER" to submit the comment.
    pyautogui.press('enter')

    # Move to the exit button and click it.
    pyautogui.moveTo(775, 200, duration = 1)
    pyautogui.click(775, 200)
