firstName = input("What is your first name? ")#input for first name
lastName = input("What is your last name? ")#input for last name

firstInitial = firstName[0]#creating first initial from the first name
secondInitial = lastName[0]#creating second initial from the last name

print(f"Hello, {firstName} {lastName}.")
print(f"Your first name is {len(firstName)} letters long, and your last name is {len(lastName)} letters long.")
print(f"Your initials are {firstInitial.upper()}{secondInitial.upper()}.")