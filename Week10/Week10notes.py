#Functions
# is a named set of instructions you can run whenever you want
# they let us write code once and reuse it

#define a funtion: creat one in pythond with def
#call a function: run it by naming it with () 
#Paramater: placeholdervaraible inside funtion definition
#Argument: real valu passed in when called

#Define a funtion

# def hello():
#     print("Hello")

# hello()


#arfuments and parameters
#function to greet by name

# def greet(name):
#     print(f"Hello, {name}")

# greet("David")


#Why are functions useful?
#reuse code, not copy and paste lots of code
#organization, allows program to become more readable
#breaking big problems into smaller ones

# print("Welcome")
# print("pick an option")
# print("goodbye")


# def showMenu():
#     print("Welcome")
#     print("pick an option")
#     print("goodbye")

# showMenu()



#print vs return
#a function to print

# def helloWorld():
#     print("Hello")
# #Shows text to user, but doesnt give value back to rest of program

# #function to return

# def helloReturn():
#     return "Hello World"
# #sends value to where funtion was called, so it can be accessed later
# #Print is for user, return is for program

# msg = helloReturn()
# print(msg)

# result = helloWorld()
# print(helloWorld())


# #Calc funtion with two paramaters, will have if/elif based on operator

# def calFunc(num1, num2):
#     operator = input("Choose an opperation: +, -, *, /")
    #use if and elif to decide what to do, do the math, and print/return result


#fake loop: function calling itself
#function call call itself, called recursion
#behaves like loop if repeats until condition is met


def playAgain():
    #user to be promtped with question , if y then reprompt, if n then break out of loop
    question = input("Do you with to keep playing? y/n").lower()
    if question == "y":
        playAgain()
    else:
        print("Goodbye")

playAgain()