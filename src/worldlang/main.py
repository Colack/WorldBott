import sys
import os
import time

variables = []

def getFileInput():
    # Get the file name from the user
    fileName = input("Enter the file name: ")
    try:
        file = open(fileName, "r")
        # Make sure file ends with '.wut'
        if fileName.endswith(".wut"):
            time.sleep(0.1)
        else:
            print("File must end with '.wb'")
            return getFileInput()
        if file.read() == "":
            print("File is empty")
            return getFileInput()
        else:
            time.sleep(0.1)
        compile(file)
    except FileNotFoundError:
        print("File not found")
        return getFileInput()

def compile(file):
    # Read the file line by line, translate the code and put it in a python file
    fileName = file.name
    # Create a new file 
    newFile = open(fileName[:-4] + ".py", "w")
    # Start writing to the new file
    newFile.write("#!/usr/bin/env python3\n")
    newFile.write("# Path: " + fileName[:-4] + ".py\n")
    # Read the file line by line and translate the code
    for line in file:
        # Remove the newline character
        line = line.rstrip()
        if line.startswith("~"):
            # If the line is a comment, ignore it
            continue
        elif line.startswith("int"):
            # If the line is an integer, just make it a regular variable
            newFile.write(line[4:] + "\n")
            # Append the variable to the list of variables
            variables.append(line[4:])
        elif line.startswith("str"):
            # If the line is a string, just make it a regular variable
            newFile.write(line[4:] + "\n")
            # Append the variable to the list of variables
            variables.append(line[4:])
        elif line.startswith("float"):
            # If the line is a float, just make it a regular variable
            newFile.write(line[6:] + "\n")
            # Append the variable to the list of variables
            variables.append(line[6:])
        elif line.startswith("bool"):
            # If the line is a boolean, just make it a regular variable
            newFile.write(line[5:] + "\n")
            # Append the variable to the list of variables
            variables.append(line[5:])
        elif line.startswith("log"):
            # Turn the line into a print statement
            newFile.write("print" + line[4:] + "\n")
        elif line.startswith("if"):
            # Turn the line into an if statement
            newFile.write("if " + line[3:] + ":\n")
        elif line.startswith("else"):
            # Turn the line into an else statement
            newFile.write("else:\n")
        elif line.startswith("else if"):
            # Turn the line into an else if statement
            newFile.write("elif " + line[7:] + ":\n")
        elif line.startswith("while"):
            # Turn the line into a while statement
            newFile.write("while " + line[6:] + ":\n")
        elif line.startswith("for"):
            # Turn the line into a for statement
            newFile.write("for " + line[4:] + ":\n")
        elif line.startswith("break"):
            # Turn the line into a break statement
            newFile.write("break\n")
        elif line.startswith("continue"):
            # Turn the line into a continue statement
            newFile.write("continue\n")
        elif line.startswith("return"):
            # Turn the line into a return statement
            newFile.write("return " + line[7:] + "\n")
        elif line.startswith("func"):
            # Turn the line into a function
            newFile.write(line[3:] + ":\n")
        elif line.startswith("call"):
            # Turn the line into a function call
            newFile.write(line[4:] + "\n")
        elif line.startswith("end"):
            # Turn the line into an end statement
            newFile.write("\n")
        elif line.startswith("include"):
            # Turn the line into an include statement
            newFile.write("import " + line[7:] + "\n")
        elif line.startswith("sleep"):
            # Turn the line into a sleep statement
            newFile.write("time.sleep(" + line[5:] + ")\n")
        elif line.startswith("terminal"):
            # Check to see what is after the '.'
            if line[9:] == "clear":
                # If it is 'terminal.clear', clear the terminal
                newFile.write("os.system('clear')\n")
            elif line[9:] == "exit":
                # If it is 'terminal.exit', exit the program
                newFile.write("sys.exit()\n")
            elif line[9:] == "print":
                # If it is 'terminal.print', print the next line
                newFile.write("print(input())\n")
            elif line[9:] == "input":
                # If it is 'terminal.input', get input from the user
                newFile.write("input()\n")
            elif line[9:] == "clearLine":
                # If it is 'terminal.clearLine', clear the line
                newFile.write("print('\\r' * len(input()))\n")
            elif line[9:] == "clearLineBack":
                # If it is 'terminal.clearLineBack', clear the line back
                newFile.write("print('\\r' * len(input()))\n")
            elif line[9:] == "clearLineForward":
                # If it is 'terminal.clearLineForward', clear the line forward
                newFile.write("print('\\r' * len(input()))\n")
            elif line[9:] == "clearLineBackward":
                # If it is 'terminal.clearLineBackward', clear the line backward
                newFile.write("print('\\r' * len(input()))\n")
        elif line.startswith("math"):
            # Turn the line into a math statement
            newFile.write(line[4:] + "\n")
        elif line.startswith("rand"):
            # Turn the line into a random statement
            newFile.write(line[4:] + "\n")
        elif line.startswith("randint"):
            # Turn the line into a random integer statement
            newFile.write(line[7:] + "\n")
        elif line.startswith("randfloat"):
            # Turn the line into a random float statement
            newFile.write(line[8:] + "\n")
        elif line.startswith("randbool"):
            # Turn the line into a random boolean statement
            newFile.write(line[8:] + "\n")
        elif line.startswith("randstr"):
            # Turn the line into a random string statement
            newFile.write(line[7:] + "\n")
        elif line.startswith("randint"):
            # Turn the line into a random integer statement
            newFile.write(line[7:] + "\n")
        else:
            # Check if the line is a variable
            if line in variables:
                # If it is, just write it to the new file
                newFile.write(line + "\n")
            else:
                # If it isn't, log an error and exit.
                print("Error: " + line + " is not a variable")
                # delete the new file
                os.remove(fileName[:-4] + ".py")
                sys.exit()
        
    
    
