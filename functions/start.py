# Start and Login
def start():
    # Print the name and version of the bot.
    print("WorldBott " + version + " is starting...")

    # Close visual studio code
    pyautogui.moveTo(1760, 0, duration = 1)
    pyautogui.click(1760, 0)

    # Move to the username field
    pyautogui.moveTo(1032, 280, duration = 1)
    pyautogui.click(1032, 280)

    # Type the username
    pyautogui.typewrite(username)

    # Move to the password field
    pyautogui.moveTo(1032, 325, duration = 1)
    pyautogui.click(1032, 325)

    # Type the password
    pyautogui.typewrite(password)

    # Hit the login button
    pyautogui.moveTo(1032, 380, duration = 1)
    pyautogui.click(1000, 380)  

    # Successfully logged in
    print("WorldBott has successfully logged in!")
    print("Starting the main script...")

    # Start the script
    main()
