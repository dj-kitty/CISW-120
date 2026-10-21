#task 1
def greet_user(name):
    print(f"Hello, {name}")

name = input("What is your name?  ")
greet_user(name)





#task 2 and 4

def function_calc(num1, num2):
    operation = input("What operation would you like to perform? (+, -, *, /) ")
 #operations
    if operation == "+":
        result = num1 + num2
        print(result)
    elif operation == "-":
        result = num1 - num2
        print(result)
    elif operation == "*":
        result = num1 * num2
        print(result)
    elif operation == "/":
        result = num1 / num2
        print(result)
    else:
        print("Invalid input. Please try again.")
        function_calc(num1, num2)

    keep_going = input("Would you like to keep going? (y/n)").lower()
    if keep_going == "y": #fake loop
        function_calc(num1, num2)
    else:
        print("Goodbye")

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

function_calc(num1, num2)




#Task 3

def get_length(text):
    num_of_chars = len(text) #get length of text
    return num_of_chars

data = input("Please input some text: ")
length = get_length(data)
print(f"Your text was {length} characters long")