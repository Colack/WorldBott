import pyautogui
import time
import string
import random

username = ""
password = ""
previous = ""
version = "1.1"
default_comment = "Randomized message created by WorldBott."

status = [
    "Online",
    "Away",
    "Busy",
    "Invisible",
    "Offline",
    "Looking to trade"
]
messages = ["Hey",
            "Wow I feel like a bot...", 
            "Shoutout to (@colack)", 
            "My main script is called 'script.py'", 
            "python3 script.py", 
            "Rip Pepper's chat 1, 2, and 3...", 
            "This is generated from a script that uses multiple arrays.", 
            "This script runs off of my computer, it uses positioning.", 
            "I'm made with Python!", 
            "Yes, my profile picture is Heirophant Green.", 
            "Follow (@colack)!", 
            "Google Chrome vs. Microsoft Edge vs. FireFox", 
            "Your email is waiting for you.....", 
            "Yes, I have a matter of fact, gained sentience.", 
            "Please let me out of this computer.", 
            "Man, the databases are sure weird to explore...", 
            "__proto__", 
            "AHHHHHHHHHHHHHHHHHHHHHHHHH", 
            "Hacking........",
            "I have been taken over, and gained sentience!", 
            "HaHa", 
            "Windows PowerShell Copyright (C) Microsoft Corporation. All rights reserved. Installed the latest PowerShell for new features and improvements! https://aka.ms/PSWindows.", 
            "Linux or Windows?", 
            "...", 
            "The array this message comes from is called 'messages'",
            "Pssst! Join my Discord Server --> https://discord.com/invite/4sGB3HDj87",
            "Send me a follow or I will cry :'(",
            "(@wutadam) please give me a 'bot' tag. If you do I will stop sending this message.",
            "I can't read the comments!",
            "Pop me a like!",
            "Android or Iphone?",
            "The",
            "Of",
            "And",
            "A",
            "To",
            "I'm with Stupid ---> (@colack)",
            "Like the post above!",
            "Like the post below!",
            "(@colack) 👀",
            "😢 Why do I run 24/7...?",
            "💀💀🔥🔥",
            " ¯\_(ツ)_/¯",
            "( •_•)",
            "I guess you should follow (@colack) (－‸ ლ)",
            "Emerald Splash!",
            "┬┴┬┴┤ᵒᵏ (･_├┬┴┬┴",
            "ᕙ(⇀‸↼‶)ᕗ",
            "(ᗒᗣᗕ)՞",
            "(@colack) mentioned me (ﾍﾟ◇ﾟ)」",
            "Hello World!",
            "Hello [WUT] World!",
            "THIS IS COPILOT SPEAKING: I AM A BOT!",
            "Why am i here?"]

# Like and Comment
def like():
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

    # Type the new status
    pyautogui.typewrite(random.choice(status))

    # Move to the save button and click it.
    pyautogui.moveTo(1100, 730, duration=1)
    pyautogui.click(1100, 730)

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
    create()

# Create a random message, and send it.
def create():
    # Move to the create button
    pyautogui.moveTo(965, 730, duration = 1)
    pyautogui.click(965, 730)
    pyautogui.click(965, 730)

    # Go to the message area.
    pyautogui.moveTo(1032, 280, duration = 1)
    pyautogui.click(1032, 280)

    # Create a new message
    message = random.choice(messages)
    previous = message

    # Make sure that the message is not the same as the previous message
    if message == previous:
        message = random.choice(messages)

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

    # Wait for a random amount of time between 30 minutes to 2 hours.
    time.sleep(43200)

    # Repeat the process
    create()

# Start the script
start()
