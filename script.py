import os
import sys
import pyautogui
import random
import string
import time

username = "username"
password = "password"
made = False
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
            "(@colack) mentioned me (ﾍﾟ◇ﾟ)」"]

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
