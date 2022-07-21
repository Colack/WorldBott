import os
import sys
import pyautogui
import random
import time

username = "username"
password = "password"
made = False
messages = ["Hey", "Wow I feel like a bot...", "Shoutout to (@colack)", "My main script is called 'script.py'", "python3 script.py", "Rip Pepper's chat 1, 2, and 3...", "This is generated from a script that uses multiple arrays.", "This script runs off of my computer, it uses positioning.", "I'm made with Python!", "Yes, my profile picture is Heirophant Green.", "Follow (@colack)!", "Google Chrome vs. Microsoft Edge vs. FireFox", "Your email is waiting for you.....", "Yes, I have a matter of fact, gained sentience.", "Please let me out of this computer.", "Man, the databases are sure weird to explore...", "__proto__", "AHHHHHHHHHHHHHHHHHHHHHHHHH", "Hacking........", "I have been taken over, and gained sentience!"]

def start():
    pyautogui.moveTo(1760, 0, duration = 1)
    pyautogui.click(1760, 0)
    pyautogui.moveTo(1032, 280, duration = 1)
    pyautogui.click(1032, 280)
    pyautogui.typewrite(username)
    pyautogui.moveTo(1032, 325, duration = 1)
    pyautogui.click(1032, 325)
    pyautogui.typewrite(password)
    pyautogui.moveTo(1032, 380, duration = 1)
    pyautogui.click(1000, 380)  

def create():
    pyautogui.moveTo(965, 730, duration = 1)
    pyautogui.click(965, 730)
    pyautogui.click(965, 730)
    pyautogui.moveTo(1032, 280, duration = 1)
    pyautogui.click(1032, 280)
    message = random.choice(messages)
    pyautogui.typewrite(message)
    pyautogui.moveTo(1100, 400, duration = 1)
    pyautogui.click(1100, 400)
    time.sleep(120)
    create()

start()
create()
