#This simple program asks for the user's first and last name and age,
#and then estimates their birth year based on the current year and their age.
#Then it asks for the user to comfirm the estimated birth year, and corrects it if necessary.
#Created by David Johnson on September 1 2026

firstName = input("What is your first name? ")
lastName = input("What is your last name? ")
fullName = firstName + " " + lastName #concatenation of first and last name

print(f"Hello, {fullName}")

age = input("What is your age? ")

print(f"Hello, {fullName}, you are {age} years old.")

currentYear = 2026
estimatedBirthYear = currentYear - int(age) #estimating birth year

correct = input(f"You were born in {estimatedBirthYear}, right? (yes/no) ")

if correct.lower() == "yes": #if input is yes, this part runs
    print("Yay! I guessed right!")
elif correct.lower() == "no":#if input is no, this part runs
    birthYear = input("Ah man! What is your actual birth year? ")
    print(f"So, {fullName}, you are {age} years old and were born in {birthYear}.")
    #if input is neither yes nor no, an error will be thrown, 
    #but I do not yet know how to do repeating functions yet
    #so hopefully the input will be yes or no.
