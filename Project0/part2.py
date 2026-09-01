print("This is a simple calculator program.")
print("You will be asked for two numbers, and then what operation you want to do.")

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

print("Here are your options:")#list the options
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = input("Please enter the number of the operation you want to perform (1-4): ")

#the following if statements will use the input from above to determine what operation to perform and then print the result

if operation == "1":#1=addition
    result = float(num1) + float(num2)
elif operation == "2":#2=subtraction
    result = float(num1) - float(num2)
elif operation == "3":#3=multiplication
    result = float(num1) * float(num2)
elif operation == "4":#4=division
    if float(num2) == 0:#since division by zero is not allowed, this will check if the second number is zero and print an error message if it is
        print("Error: Division by zero is not allowed.")
        result = None
    else:
        result = float(num1) / float(num2)

if result is not None:#this runs if an error message is not thrown by the division section
    print(f"The result of the operation is: {result}")#prints result of the operation