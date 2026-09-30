#what is a loop
#a loop repeats code

#repeat this loop three times

# for number in range(100):
#     #Print hello each run
#     print("Hello")

#While loops
#repeats while a condition is true

#make a program to print 1-5

# num = 1 #starting point
# while num <=5: #end point
#     print(num)
#     num +=1 #makes num increase

#start at 0, count to 50 by fives

# num2 = 0 #starting point
# while num2 <=50: #end point
#     print(num2)
#     num2 +=5 #makes num increase

#a while loop is useful when you want to keep asking until the user gives a valid answer
#ask user for age

# age = int(input("What is your age? "))

# #keep looping if age < 1 or > 120

# while age < 1 or age > 120:
#     #tell user invalid input
#     print("Invalid age. ")

#     #ask user to enter age again
#     age = int(input("What is your age? "))
# #this runs after loop finish
# print("Thank you")


#For loops
#works through items one at a time

#create a list with three games

# games = ["sudoku", "monopoly", "uno"]
# cars = ["tesla", "chevy", "Nissan"]

#print one list item at a time

# for game in games:
#     #Print current game
#     print(game)
# #each time loop repeats, game holds next item in list
# for i in cars:
#     print(i)

#range creates a sequence of numbers
#start at two, stops before 8

# for number in range(2,8): #(starting number, stop before)
#     print(number)
    #remeber ending number is not included

    #we can also perform calculations in the loop

    #Loop through numbers 2-7
# for number in range(2,8):
#     # square number
#     square = number * number
#     #Print squared number
#     print(square)

# #looping through string
# #Store name inside string
# name = "David"
# #Take characters in string one ata a time
# for letter in name:
#     print(letter)

#using break
#end a loop

#loop through numbers 1-10
# for number in range(1,11):
#     print(number)
#     if number == 5:
#         break

#nested loop
#is a loop in a loop

#OUter loop will run through 1,2,3

# for number in range(1,4):
#     #inner loop will do the same
#     for number2 in range(1,4):
#         print(number, number2)

#choosing the right loop?

#while loop when repetition depends on a condition

# #keep looping while answer ! yes
# while answer != "yes":
#     #ask user again
#     answer = input("Enter yes")

# #for loops when working through item in list
# items = ["apples" , "oranges", "Kiwis"]
# for item in items:
#     print(item)

# #use for with range when working through numbers
# #loop 1-10
# for number in range(1,11):
#     print(number)