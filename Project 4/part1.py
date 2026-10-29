#This program is an edit of a previous program with files. I added functions to read and write more cleanly
#I also added more functions to make the program more neat.
#I also moved the reading of the file outside of the true loop so that it doesn't read the file every time the user makes a choice.
#I also moved the break in the irrational number section to after option four for better readability
# Created by David Johnson for Intro to Programming

import math

def readFile():
    with open("Project 4/choices.txt", "r") as file:
        choices = file.read()
        print(f"Here are your choices so far: \n{choices}")

def addChoices(content):
    with open("Project 4/choices.txt", "a") as file:
        file.write(content + "\n")

def mainOptions():
    print("\nWhat would you like to do? Please select the number from the list below.")
    print("1: Convert a number to binary")
    print("2: Convert a number to hexadecimal")
    print("3: Learn the value of a common irrational number") 
    print("4: Exit the program")
    choice = input("Enter the number of your choice: ")
    return choice

def irrationalOptions():
    print("\nHere are some common irrational numbers:")
    print("1: Pi")
    print("2: Euler's number")
    print("3: The golden ratio")
    print("4: Square root of 2")
    print("5: Return to the main menu")
    choice = int(input("Enter the number of your choice: "))
    return choice

with open("Project 4/choices.txt", "w") as file:
    pass  # Create an empty file, or if file exists erases everything in it
        #I would have put this in with the addChoices function, but had no idea hot to make sure it only ran once

while True: 

    choice = mainOptions()

    if choice == '1':
        num = int(input("Enter a number to convert to binary: "))
        binary = bin(num)[2:]  # Convert to binary and remove the '0b' prefix, bin() function learned from https://www.w3schools.com/python/ref_func_bin.asp
        content = f"{num} in binary = {binary}"
        print(content)

    elif choice == '2':
        num = int(input("Enter a number to convert to hexadecimal: "))
        hexadecimal = hex(num)[2:]  # Convert to hexadecimal and remove the '0x' prefix, hex() function learned from https://www.w3schools.com/python/ref_func_hex.asp
        content = f"{num} in hexadecimal = {hexadecimal}"
        print(content) 

    elif choice == '3':
        while True:
            irrationalChoice = irrationalOptions()

            if irrationalChoice !=5:
                decPlace = int(input("How many decimal places would you like to see? (Max = 15): ")) #round() learned from https://www.w3schools.com/python/ref_func_round.asp
                while decPlace < 0 or decPlace > 15:
                    print("Invalid input. Please enter a number between 0 and 15.")
                    decPlace = int(input("How many decimal places would you like to see? (Max = 15): "))

            if irrationalChoice == 1:
                content = f"Pi to {decPlace} decimal places is: {round(math.pi, decPlace)}"
                print(content) #learned about math.pi from https://www.w3schools.com/python/ref_math_pi.asp
            elif irrationalChoice == 2:
                content = f"Euler's number to {decPlace} decimal places is: {round(math.e, decPlace)}"
                print(content) #learned about math.e from https://www.w3schools.com/python/ref_math_e.asp
            elif irrationalChoice == 3:
                content = f"The golden ratio to {decPlace} decimal places is: {round(math.phi, decPlace)}"
                print(content) #learned about math.phi from https://www.w3schools.com/python/ref_math_phi.asp
            elif irrationalChoice == 4:
                content = f"Square root of 2 to {decPlace} decimal places is: {round(math.sqrt(2), decPlace)}"
                print(content)
            elif irrationalChoice == 5:
                break
            else:
                print("Invalid choice. Please try again.")

            addChoices(content) #call function to add the content to the file

    elif choice == '4':
        break
    
    else:
        print("Invalid choice. Please try again.")

    addChoices(content) #call function to add the content to the file

readFile() #call function to read file and display previous choices
