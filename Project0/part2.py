print("This is a simple calculator program.")
print("You will be asked for two numbers, and then what operation you want to do.")

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

print("Here are your options:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = input("Please enter the number of the operation you want to perform (1-4): ")

if operation == "1":
    result = float(num1) + float(num2)
elif operation == "2":
    result = float(num1) - float(num2)
elif operation == "3":
    result = float(num1) * float(num2)
elif operation == "4":
    if float(num2) == 0:
        print("Error: Division by zero is not allowed.")
        result = None
    else:
        result = float(num1) / float(num2)

if result is not None:
    print(f"The result of the operation is: {result}")