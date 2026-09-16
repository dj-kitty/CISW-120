temp = float(input("What is the temperature you want to convert? "))
ogType = input("What type of temperature do you have? (F, C, K) ").upper()
newType = input("What temperature do you want to convert to? (F, C, K) ").upper()

if ogType == "F" and newType == "C": #converts F to C
    converted = (temp - 32) * (5/9)
    print(f"Converted temperature is {converted}")

if ogType == "F" and newType == "K": #converts F to K
    converted = (temp + 459.67) * (5/9)
    print(f"Converted temperature is {converted}")

if ogType == "C" and newType == "F": #converts C to F
    converted = temp * (9/5) + 32
    print(f"Converted temperature is {converted}")

if ogType == "C" and newType == "K": #Converts C to K
    converted = temp + 273.15
    print(f"Converted temperature is {converted}")

if ogType == "K" and newType == "F": #Converts K to F
    converted = temp * (9/5) - 459.67
    print(f"Converted temperature is {converted}")

if ogType == "K" and newType == "C": #Converts K to C
    converted = temp - 273.15
    print(f"Converted temperature is {converted}")

else:
    print("Invalid input. Please try again") #this runs if no conversion can be done due to incorrect input