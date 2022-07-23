# Take the message and post it.
def main():
    # Move to the create button
    pyautogui.moveTo(965, 730, duration = 1)
    pyautogui.click(965, 730)
    pyautogui.click(965, 730)

    # Go to the message area.
    pyautogui.moveTo(1032, 280, duration = 1)
    pyautogui.click(1032, 280)

    # Make a new message
    create()

    # Make sure that the message is not the same as the previous message.
    while message == previous:
        create()

    # Message is now created.
    print("Creating new message...")
    
    # We will now make sure that the message is not too long.
    if len(message) > 140:
        # If the message is too long, we will truncate it.
        message = message[:140]
        # Add a "..." to the end of the message.
        message = message + "..."
    else:
        # If the message is not too long, we will leave it as is.
        pass

    # We will also make sure that the message is not too short.
    if len(message) < 3:
        # If the message is too short, we will add a "..." to the end of the message.
        message = message + "..."
    else:
        # If the message is not too short, we will leave it as is.
        pass
    
    # Type the message    
    pyautogui.typewrite(message)

    # Hit the post button
    pyautogui.moveTo(1100, 400, duration = 1)
    pyautogui.click(1100, 400)

    # Wait a bit for the message to be posted.
    time.sleep(10)

    # Like and comment on the message.
    like()

    # Change the current status to a new status.
    statusChange()

    # Wait 12 hours to post again.
    time.sleep(43200)

    # Repeat the process
    create()
