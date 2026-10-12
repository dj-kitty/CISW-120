#This program allows the user to convert a number to binary or hexadecimal, as well as learn the value of some common irrational numbers to a specified number of decimal places. The user can choose to exit the program at any time.
#Created by David Johnson for Intro to Programming

import math

while True:
    print("\nWhat would you like to do? Please select the number from the list below.")
    print("1: Convert a number to binary")
    print("2: Convert a number to hexadecimal")
    print("3: Learn the value of a common irrational number")
    print("4: Exit the program")
    choice = input("Enter the number of your choice: ")

    if choice == '1':
        num = int(input("Enter a number to convert to binary: "))
        binary = bin(num)[2:]  # Convert to binary and remove the '0b' prefix, bin() function learned from https://www.w3schools.com/python/ref_func_bin.asp
        print(f"{num} in binary is: {binary}")

    elif choice == '2':
        num = int(input("Enter a number to convert to hexadecimal: "))
        hexadecimal = hex(num)[2:]  # Convert to hexadecimal and remove the '0x' prefix, hex() function learned from https://www.w3schools.com/python/ref_func_hex.asp
        print(f"{num} in hexadecimal is: {hexadecimal}")

    elif choice == '3':
        while True:
            print("\nHere are some common irrational numbers:")
            print("1: Pi")
            print("2: Euler's number")
            print("3: The golden ratio")
            print("4: Square root of 2")
            print("5: Return to the main menu")
            irrationalChoice = int(input("Enter the number of your choice: "))

            if irrationalChoice == 5: #set this before asking for number of decimal places
                break

            decPlace = int(input("How many decimal places would you like to see? (Max = 15): ")) #round() learned from https://www.w3schools.com/python/ref_func_round.asp
            while decPlace < 0 or decPlace > 15:
                print("Invalid input. Please enter a number between 0 and 15.")
                decPlace = int(input("How many decimal places would you like to see? (Max = 15): "))

            if irrationalChoice == 1:
                print(f"Pi to {decPlace} decimal places is: {round(math.pi, decPlace)}") #learned about math.pi from https://www.w3schools.com/python/ref_math_pi.asp
            elif irrationalChoice == 2:
                print(f"Euler's number to {decPlace} decimal places is: {round(math.e, decPlace)}") #learned about math.e from https://www.w3schools.com/python/ref_math_e.asp
            elif irrationalChoice == 3:
                print(f"The golden ratio to {decPlace} decimal places is: {round(math.phi, decPlace)}") #learned about math.phi from https://www.w3schools.com/python/ref_math_phi.asp
            elif irrationalChoice == 4:
                print(f"Square root of 2 to {decPlace} decimal places is: {round(math.sqrt(2), decPlace)}")
            else:
                print("Invalid choice. Please try again.")

    elif choice == '4':
        break
    
    else:
        print("Invalid choice. Please try again.")