import pyautogui
import time
import string
import random
import requests

username = ""
password = ""
previous = ""
version = "1.1"
default_comment = "Randomized message created by (@WorldBott). Contact (@colack) if you want to suggest a new message. (Or Template!)"
default_status = "Hi There! I'm WorldBott!\nI'm a bot created by (@colack).\nI use DeepAI and a lot of pre-generated messages to create random status updates.\n\nContact (@colack) if you want to suggest a new message.\n\nI'm currently running version " + version + "."
prompts = [
    "Hi there, I'm WorldBott!",
    "I'm WorldBott!",
    "Today, I was communicating with some APIs and I got this message.",
    "I really like Visual Studio code because: ",
    "I'm a bot created by (@colack)",
    "Today I was wondering",
    "I'm currently thinking about",
    "I was talking to",
    "I'm currently talking to",
    "I might have done"
]

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

# Create a new message
def create():
    # Create a random number between 1 and 5.
    random_number = random.randint(1, 10)
    
    if random_number == 1:
        # Create a random string of numbers and letters
        random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1, 10)))
        message = random_string + " <-- My new favorite word!"
        previous = message
    elif random_number == 2:
        message = "I'm a bot created by (@colack)"
        previous = message
    elif random_number == 3:
        # Grab a random dad joke of the internet.
        url = "https://icanhazdadjoke.com/"
        responce = requests.get(url, headers={"Accept": "application/json"})
        message = responce.json()['joke']
        previous = message
    elif random_number == 4:
        message = "✌(ツ)"
        previous = message
    elif random_number == 5:
        message = "🤖"
        previous = message
    elif random_number == 6:
        message = "Don't forget, if you want to suggest a new message, contact (@colack)!"
        previous = message
    else:
        # Grab a random prompt and send it to the deep ai model.
        r = requests.post(
            "https://api.deepai.org/api/text-generator",
        data={
            'text': random.choice(prompts),
        },
            headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
        )
        message = r.json()['output']
        previous = message

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

# Start the script
start()
