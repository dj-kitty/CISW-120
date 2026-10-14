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
        content = f"{num} in binary = {binary}"
        print(content)

    elif choice == '2':
        num = int(input("Enter a number to convert to hexadecimal: "))
        hexadecimal = hex(num)[2:]  # Convert to hexadecimal and remove the '0x' prefix, hex() function learned from https://www.w3schools.com/python/ref_func_hex.asp
        content = f"{num} in binary = {hexadecimal}"
        print(content)

    elif choice == '3':
        while True:
            print("\nHere are some common irrational numbers:")
            print("1: Pi")
            print("2: Euler's number")
            print("3: The golden ratio")
            print("4: Square root of 2")
            print("5: Return to the main menu")
            irrationalChoice = int(input("Enter the number of your choice: "))

            with open("Week9/choices.txt", "r") as file:
                choices = file.read()
                print(f"Here are your choices so far: \n{choices}")

            if irrationalChoice == 5: #set this before asking for number of decimal places
                break
            with open("Week9/choices.txt", "a") as file:
                file.write(content + "\n")
            
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
            else:
                print("Invalid choice. Please try again.")
    elif choice == '4':
        with open("Week9/choices.txt", "r") as file:
            choices = file.read()
            print(f"Here are your choices: \n{choices}")
        break
    
    else:
        print("Invalid choice. Please try again.")

    with open("Week9/choices.txt", "a") as file:
        file.write(content + "\n")
    with open("Week9/choices.txt", "r") as file:
        choices = file.read()
        print(f"Here are your choices so far: \n{choices}")


