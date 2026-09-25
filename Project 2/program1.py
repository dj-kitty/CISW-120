#This is a simple calculator program.
#It performs basic arithmetic operations such as addition, subtraction, multiplication, and division, as well as exponents, square root, and logarithms.
#Created by David Johnson for Intro to Programming

import math #this is for the operations besides addition, subtraction, multiplication, division, and exponents
#Learned from https://www.w3schools.com/python/python_math.asp 
#Knowledge of imports used from prior programming experience

print("What kind of operation would you like to perform? Please select the number from the list below.") #the options
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")
print("5: Exponent")
print("6: Square Root")
print("7: Logarithm (base 10)")
print("8: Natural Logarithm (base e)")

operation = int(input("Enter the number of the operation you would like to perform: "))

if operation == 1 or operation == 2 or operation == 3 or operation == 4 or operation == 5: #if the operation requires two numbers, this will run
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
else:
    num1 = float(input("Enter the number: ")) #if not, this will run

if operation == 1:
    result = num1 + num2
    print(f"The result of adding {num1} and {num2} is: {result:.2f}")
elif operation == 2:
    result = num1 - num2
    print(f"The result of subtracting {num2} from {num1} is: {result:.2f}")
elif operation == 3:
    result = num1 * num2
    print(f"The result of multiplying {num1} and {num2} is: {result:.2f}")
elif operation == 4:
    if num2 == 0:
        print("Error: Division by zero is not allowed.") #since division by zero is undefined
    else:
        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is: {result:.2f}")
elif operation == 5:
    result = num1 ** num2
    print(f"The result of raising {num1} to the power of {num2} is: {result:.2f}")
elif operation == 6:
    if num1 < 0:
        print("Error: Square root of a negative number is not defined in real numbers.")
    else:
        result = math.sqrt(num1)
        print(f"The square root of {num1} is: {result:.2f}")
elif operation == 7:
    if num1 <= 0:
        print("Error: Logarithm is not defined for zero or negative numbers.")
    else:
        result = math.log10(num1)
        print(f"The base 10 logarithm of {num1} is: {result:.2f}")
elif operation == 8:
    if num1 <= 0:
        print("Error: Natural logarithm is not defined for zero or negative numbers.")
    else:
        result = math.log(num1)
        print(f"The natural logarithm of {num1} is: {result:.2f}")