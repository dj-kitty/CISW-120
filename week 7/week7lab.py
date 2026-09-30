#This is the lab for week 7, created by David Johnson for Intro to Programming

number = 1
while number <= 5:
    print(number)
    number += 1

print()#added empty lines for better results readability

isHuman = input("Are you human? (This should be yes) ").lower()
while isHuman != "yes": #and thus if not human
    print("Invaid input. Please try again.")
    isHuman = input("Are you human? (This should be yes) ").lower()

print()

fruits = ["Oranges", "Apples", "Bananas"]
for fruit in fruits:
    print(fruit)

print()

for num in range(2,8):
    square = num * num
    print(f"{num} -> {square}")

print()

name = "David"
for letter in name:
    print(letter)

print()

for i in range(1,11):
    print(i)
    if i == 7:
        break

print()

for t in range(1,4):
    for k in range(1,4):
        print(t, k) 

#the first loop runs and sets t to a number. then the inner loop runs the speficied number of times and prints the first number and the changing second number
#Then the first loop repeats and changes the first number, with the second loop repeating