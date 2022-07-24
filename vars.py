from imports import *

# This file contains all of the Variables that the bot Uses.

# ~~ Oraganization ~~

# Why does Python not have a #DEFINE statement?

# API KEY
key = ""

# Username and Password
username = ""
password = ""

# Starting Message.
starting_message = "<-- WorldBott has Woken Up! -->"

# Window Names
WINDOW_PROMPT = "WorldBott Prompt"
WINDOW_USERNAME = "Username Input"
WINDOW_PASSWORD = "Password Input"
WINDOW_CLOSE_VS_CODE = ""
WINDOW_RELOAD = ""
WINDOW_TEST_TIME = ""

# Upcoming Features
TODO = [
    "Add a way to change the username and password using a GUI",
    "Add a way to change the starting message using a GUI",
    "Add a way to change the API key using a GUI",
    "Add new custom messages using a GUI",
    "Have custom messages be stored inside of a text file.",
    "Give the bot the ability to read comments.",
    "Give the bot the ability to read posts.",
    "Give the bot the ability to read messages.",
    "Give the bot the ability to read likes.",
    "Have the bot grab its own link, communicate with a Discord bot, and send messages to a Discord channel.",
    "Discord Integration?",
    "Get the bot a custom nameplate.",
    "Get the bot a 'bot' role.",
    "Get the bot to follow other users.",
    "Have the bot communicate with another bot."
]

# Completed Features
COMPLETED = [
    "The Bot can close VS Code.",
    "The Bot can reload the page.",
    "The Bot can test the time values.",
    "The Bot can go to a specific field.",
    "The Bot can log itself in.",
    "The Bot can send messages, and custom images.",
    "The Bot can send custom messages.",
    "The Bot can use API's to get information, then post about that information.",
    "The Bot can like, and comment on its own posts.",
    "The Bot has its own GUI. (SomeWhat Completed)",
    "The Bot can select text, and delete it.",
    "The Bot has a developer mode."
]

# Maximum Values
MAX_POSTS = 100
MAX_LIKES = 100
MAX_COMMENTS = 100
MAX_TEXT = 500

# Minimum Values
MIN_POSTS = 1
MIN_LIKES = 1
MIN_COMMENTS = 1
MIN_TEXT = 3

# Number Values
LOW_RAND = 1
HIGH_RAND = 15

# Time Values
WAIT_TIME = 86400
RELOAD_TIME = 10
HIGH_TIME = 5.5
LOW_TIME = 1.5
QUICK_TIME = 0.5

# Title of the Window
TITLE = "WorldBott"

# Window Size
WINDOW_X = 100
WINDOW_Y = 50

# Default Element Sizes
DEFAULT_WIDTH = 20
DEFAULT_HEIGHT = 2

# Current Version of the Bot.
version = "2.0"
num_version = 2.0

# Defaults
default_comment = "AI-Generated message created by (@WorldBott). Contact (@colack) if you want to suggest a new message. (Or Template!)"
default_status = "Hi There! I'm WorldBott!\nI'm a bot created by (@colack).\nI use DeepAI and a lot of pre-generated messages to create random status updates.\n\nContact (@colack) if you want to suggest a new message.\n\nI'm currently running version " + version + "."
default_message = ":)"

# Prompts for the Deep AI.
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

# Custom Messages 
custom_message = [

]

# Default Messages
default2 = "I'm a bot created by (@colack)"
default4 = "✌(ツ)"
default5 = "🤖"
default6 = "Don't forget, if you want to suggest a new message, contact (@colack)!"
defaultPrevious = "I'm sorry, I couldn't find a new message for you."
defaultRandom = "Here is a random image: "
defaultRandString = " <-- My new favorite word!"

# Josuke Laugh Meme
josuke_laugh = "https://i.kym-cdn.com/photos/images/original/001/177/975/e0e.gif"

# GUI WILL BE IMPLEMENTED SOON!
# Just wait ~1-Week

# Window Layout
layout = [
    [sg.Text("WorldBott Version " + version)],
    [sg.Button("Start")], [sg.Button("Exit")],
    [sg.Text("Username"), sg.InputText(key="username")],
    [sg.Text("Password"), sg.InputText(key="password")],
    [sg.Button("Submit"), sg.Button("Submit")],
]
