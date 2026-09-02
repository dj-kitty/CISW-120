# Part 1: Math

numInt = 548
numFloat = 74.65
#You can do math with both an int and a float

sum = numInt + numFloat#adds the two numbers
print(sum)

numInt = int(input("Please enter a whole number: "))#new int input, converting it to int variable
numFloat = float(input("Please enter a decimal number: "))# new float input, converting it to float variable

newSum = numInt + numFloat#adds new numbers
print(newSum)

# Part 2: Strings - Indexing and Slicing

# A string is a text variable

text = "HELLO WORLD" 
lowerText = text.lower()#turns text to lowercase

print(lowerText)

greeting = text[0:5] #takes greeting from the text and makes it a variable
print(greeting)

# Part 3: Lists

# a list can contain anything

veggies = ["carrots", "broccoli", "corn"]#original list
print(veggies)
veggies.append("orange")#adding item

print(veggies)

veggies.remove("orange")#removing item

print(veggies)

print(len(veggies))#prints how many items are in the list


# Variables can be converted to different data types for easier access. 
# Strings can be directly edited and separated, which could be useful for making a database
# Strings can be forced into a specific case, which would be helpful in eliminating user error
# When adding items to a list, they stay in the same order they were added in, which would also make this useful for a database