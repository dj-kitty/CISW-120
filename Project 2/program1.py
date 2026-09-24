import math #this is for the operations besides addition, subtraction, multiplication, division, and exponents
#Learned from https://www.w3schools.com/python/python_math.asp 

print("What kind of operation would you like to perform? Please select the number from the list below.")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")
print("5: Exponent")
print("6: Square Root")
print("7: Sine")
print("8: Cosine")
print("9: Tangent")
print("10: Inverse Sine")
print("11: Inverse Cosine")
print("12: Inverse Tangent")
print("13: Logarithm (base 10)")
print("14: Natural Logarithm (base e)")

operation = int(input("Enter the number of the operation you would like to perform: "))

if operation == 1 or operation == 2 or operation == 3 or operation == 4 or operation == 5:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
else:
    num1 = float(input("Enter the number: "))

if operation == 7 or operation == 8 or operation == 9 or operation == 10 or operation == 11 or operation == 12:
    typeOfAngle1 = input("Is your angle in degrees or radians? (Enter 'degrees' or 'radians'): ")
    typeOfAngle2 = input("What do you want your second angle to be? (Enter 'degrees' or 'radians'): ")

if operation == 1:
    result = num1 + num2
    print(f"The result of adding {num1} and {num2} is: {result}")
elif operation == 2:
    result = num1 - num2
    print(f"The result of subtracting {num2} from {num1} is: {result}")
elif operation == 3:
    result = num1 * num2
    print(f"The result of multiplying {num1} and {num2} is: {result}")
elif operation == 4:
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is: {result}")
elif operation == 5:
    result = num1 ** num2
    print(f"The result of raising {num1} to the power of {num2} is: {result}")
elif operation == 6:
    if num1 < 0:
        print("Error: Square root of a negative number is not defined in real numbers.")
    else:
        result = math.sqrt(num1)
        print(f"The square root of {num1} is: {result}")
elif operation == 7:
    m