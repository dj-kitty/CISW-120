# Intro to Programming
# Debug Exercise 2

# This program should add three numbers together.

# total = 0
# num1 = input("What's the first number? >")
# total = num1
# num2 = input("What's the second number? >")
# total = num2
# num3 = input("What's the third number? >")
# total = num3
# print(f"Total is: {total}")

total = 0
num1 = input("What's the first number? >")
total += int(num1) 
num2 = input("What's the second number? >")
total += int(num2)
num3 = input("What's the third number? >")
total += int(num3)
print(f"Total is: {total}")

#What I did is changed the = to += to add the number to the total instead of replacing it
#Then I converted the numbers to int values with the int() function
#that made it so the numbers could be added together.