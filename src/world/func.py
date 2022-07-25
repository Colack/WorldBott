from imports import *
from vars import *

# This file contains all of the functions that the bot uses.

# GUI that the bot uses to select certain options.
def start_app():
    close = sg.popup_yes_no("Minimize Visual Studio Code?", WINDOW_CLOSE_VS_CODE)
    if close == "Yes":
        closeVsCode()
    else:
        print("Not closing VS Code.")
    reload_ = sg.popup_yes_no("Reload the web page?", WINDOW_RELOAD)
    if reload_ == "Yes":
        reload()
    else:
        print("Not reloading the page.")
    start()

# List all possible nameplates.
def listNameplates():
    print("Nameplates:")
    for i in nameplate_list:
        print(i)
    print("")
    time.sleep(QUICK_TIME)

# Ask if the user wants to Quit Operations.
def quitAsk():
    quit_ = sg.popup_yes_no("Quit Operations?", WINDOW_QUIT)
    if quit_ == "Yes":
        print("Aborting...")
        quit()
    else:
        print("Not quitting.")
    time.sleep(QUICK_TIME)
    main()

# Print Lists
def printLists(type):
    if type == "TODO":
        print("TODO:")
        for i in TODO:
            print(i)
    elif type == "DONE":
        print("COMPLETED:")
        for i in COMPLETED:
            print(i)

# -MAIN STARTING FUNCTION-
def megaStart(type):
    if type == "reg":
        # Start the bot in dev mode.
        start_app()
    elif type == "easy":
        closeVsCode()
        start()

# Prints all variables to the console.
def printValues():
    print("Key: " + key)
    print("Username: " + username)
    print("Password: " + password)
    print("Starting Message: " + starting_message)
    print("Window Prompt: " + WINDOW_PROMPT)
    print("Window Username: " + WINDOW_USERNAME)
    print("Window Password: " + WINDOW_PASSWORD)
    print("Window Close VS Code: " + WINDOW_CLOSE_VS_CODE)
    print("Window Reload: " + WINDOW_RELOAD)
    print("Window Test Time: " + WINDOW_TEST_TIME)
    print("Window Quit: " + WINDOW_QUIT)
    print("Max Posts: " + str(MAX_POSTS))
    print("Max Comments: " + str(MAX_COMMENTS))
    print("Max Likes: " + str(MAX_LIKES))
    print("Max Text: " + str(MAX_TEXT))
    print("Min Posts: " + str(MIN_POSTS))
    print("Min Comments: " + str(MIN_COMMENTS))
    print("Min Likes: " + str(MIN_LIKES))
    print("Min Text: " + str(MIN_TEXT))
    print("Low Rand: " + str(LOW_RAND))
    print("High Rand: " + str(HIGH_RAND))
    print("Wait Time: " + str(WAIT_TIME))
    print("Quick Time: " + str(QUICK_TIME))
    print("Reload Time: " + str(RELOAD_TIME))
    print("High Time: " + str(HIGH_TIME))
    print("Low Time: " + str(LOW_TIME))
    print("Title: " + TITLE)
    print("WINDOW_X: " + str(WINDOW_X))
    print("WINDOW_Y: " + str(WINDOW_Y))
    
# Test different time values.
def testTime(skip):
    time.sleep(HIGH_TIME)
    print("High Time: " + str(HIGH_TIME))
    time.sleep(RELOAD_TIME)
    print("Reload Time: " + str(RELOAD_TIME))
    time.sleep(QUICK_TIME)
    print("Quick Time: " + str(QUICK_TIME))
    time.sleep(LOW_TIME)
    print("Low Time: " + str(LOW_TIME))
    if (skip == True):
        time.sleep(0.5)
        print("Skipping...")
    else:
        time.sleep(WAIT_TIME)
        print("Wait Time: " + str(WAIT_TIME))

# Close Visual Studio Code
def closeVsCode():
    # Close visual studio code
    pyautogui.moveTo(1760, 0, duration = 1)
    pyautogui.click(1760, 0)

# Reload the page.
def reload():
    # Reload the page
    pyautogui.keyDown("CTRL")
    pyautogui.press("R")

# Go to a specific field.
def field(type, click):
    if (type == "username"):
        # Move to the username field
        pyautogui.moveTo(1032, 280, duration = 1)
        if click == True:
            pyautogui.click(1032, 280)
    elif (type == "password"):
        # Move to the password field
        pyautogui.moveTo(1032, 325, duration = 1)
        if click == True:
            pyautogui.click(1032, 325)
    elif (type == "login"):
        # Hit the login button
        pyautogui.moveTo(1032, 380, duration = 1)
        if click == True:
            pyautogui.click(1032, 380) 
    elif (type == "create"):
        # Move to the create button
        pyautogui.moveTo(965, 730, duration = 1)
        if click == True:
            pyautogui.click(965, 730)
            pyautogui.click(965, 730)
    elif (type == "message"):
        # Go to the message area.
        pyautogui.moveTo(1032, 280, duration = 1)
        if click == True:
            pyautogui.click(1032, 280)
    elif (type == "post"):
        # Hit the post button
        pyautogui.moveTo(1100, 400, duration = 1)
        if click == True:
            pyautogui.click(1100, 400)
    elif (type == "sent"):
        # Click the post
        pyautogui.moveTo(775, 300, duration = 1)
        if click == True:
            pyautogui.click(775, 300)
    elif (type == "like"):
        # Move to the like button and click it.
        pyautogui.moveTo(775, 730, duration = 1)
        if click == True:
            pyautogui.click(775, 730)
    elif (type == "comment"):
        # Move to the comment box and click it.
        pyautogui.moveTo(1140, 730, duration=1)
        if click == True:
            pyautogui.click(1140, 730)
    elif (type == "comment_text"):
        pyautogui.moveTo(1140, 700, duration = 1)
        if click == True:
            pyautogui.click(1140, 700)
    elif (type == "exit"):
        pyautogui.moveTo(775, 200, duration = 1)
        if click == True:
            pyautogui.click(775, 200)
    elif (type == "profile"):
        pyautogui.moveTo(1050, 745, duration=1)
        if click == True:
            pyautogui.click(1050, 745)
    elif (type == "edit"):
        pyautogui.moveTo(800, 310, duration = 1)
        if click == True:
            pyautogui.click(800, 310)
    elif (type == "text_box"):
        pyautogui.moveTo(1032, 280, duration = 1)
        if click == True:
            pyautogui.click(1032, 280)
    elif (type == "save"):
        pyautogui.moveTo(1100, 730, duration=1)
        if click == True:
            pyautogui.click(1100, 730)

# Hit CTRL + A to select all the text.
def ctrlA():
    # Type "CTRL + A" to select all the text.
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')

# Hit DELETE to delete the text.
def delete():
    # Type "DELETE" to delete the text.
    pyautogui.keyUp('ctrl')
    pyautogui.press('delete')

# Do Both CTRL + A and DELETE
def ctrlADelete():
    ctrlA()
    time.sleep(QUICK_TIME)
    delete()

# Type some messages that the Bot Uses.
def printer(type):
    if type == "login":
        # Successfully logged in
        print("WorldBott has successfully logged in!")
        print("Starting the main script...")
    elif type == "start":
        print("WorldBott " + version + " is starting...")
    elif type == "message":
        # Message is now created.
        print("Creating new message...")

# Press ENTER
def enter():
    # Press ENTER
    pyautogui.press('enter')

# Like and Comment
def like():
    field("sent", True)
    time.sleep(QUICK_TIME)
    field("like", True)
    time.sleep(QUICK_TIME)
    field("comment", True)
    time.sleep(LOW_TIME)
    field("comment_text", True)
    pyautogui.typewrite(default_comment)
    time.sleep(LOW_TIME)
    enter()
    time.sleep(LOW_TIME)
    field("exit", True)
    time.sleep(LOW_TIME)

# Start and Login
def start():
    printer("start")
    time.sleep(HIGH_TIME)
    field("username", True)
    ctrlADelete()
    pyautogui.typewrite(username)
    time.sleep(QUICK_TIME)
    field("password", True)
    ctrlADelete()
    pyautogui.typewrite(password)
    time.sleep(QUICK_TIME)
    field("login", True)
    printer("login")
    time.sleep(LOW_TIME)
    main()

# Create a message and post it.
def main():
    print(starting_message)
    field("create", True)
    time.sleep(QUICK_TIME)
    field("message", True)
    time.sleep(QUICK_TIME)
    random_number = random.randint(LOW_RAND, HIGH_RAND)
    previous = ""
    if (previous == ""):
        # If the previous message was empty, use the default message.
        previous = default_message
    if random_number == 1:
        # Create a random string of numbers and letters
        random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1, 10)))
        message = random_string + defaultRandString
    elif random_number == 2:
        message = default2
    elif random_number == 3:
        # Grab a random dad joke of the internet.
        url = "https://icanhazdadjoke.com/"
        responce = requests.get(url, headers={"Accept": "application/json"})
        message = responce.json()['joke']
    elif random_number == 4:
        message = default4
    elif random_number == 5:
        message = default5
    elif random_number == 6:
        message = default6
    elif random_number == 7:
        # Lets just grab a random image from this website.
        url = "https://picsum.photos/200"
        responce = requests.get(url)
        url = responce.url

        # Make sure that the boolean is true.
        if (url != ""):
            url_on = True

        message = defaultRandom + url 
    else:
        # Grab a prompt from the 'prompts.txt' file.
        with open("prompts.txt", "r") as f:
            lines = f.readlines()
        random_number = random.randint(0, len(lines) - 1)
        m = lines[random_number]

        r = requests.post(
            "https://api.deepai.org/api/text-generator",
        data={
            'text': m,
        },
            headers={'api-key': key}
        )
        message = r.json()['output']
    if (message == previous):
        message = defaultPrevious
    printer("message")
    previous = message
    if len(message) > MAX_TEXT:
        message = message[:MAX_TEXT]
        message = message + "..."
    else:
        pass
    if len(message) < MIN_TEXT:
        message = message + "..."
    else:
        pass
    time.sleep(HIGH_TIME)  
    pyautogui.typewrite(message)
    time.sleep(LOW_TIME)
    field("post", True)
    time.sleep(HIGH_TIME)
    like()
    quitAsk()
    time.sleep(WAIT_TIME)
    main()
