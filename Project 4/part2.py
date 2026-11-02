#Program that asks the user for their favorite items and saves them to a text file
#Created by David Johnson for Intro to Programming


def ask(list):
    for item in list:
        if item == "car":
            answer = askCar()
        elif item == "song" or item == "book":
            title = input(f"What is your favorite {item}? ")
            author = input(f"Who is the author/artist of your favorite {item}? ")
            answer = f"{title} by {author}"
        else:
            answer = input(f"What is your favorite {item}? ")

        with open("Project 4/favorite items.txt", "a") as file:
            file.write(f"favorite {item}: {answer}\n")

def askCar():#gets all the information about the user's favorite car and returns it as a string
    make = input("What is the make of your favorite car? ")
    model = input("What is the model of your favorite car? ")
    year = input("What is the year of your favorite car? ")
    color = input("What is the color of your favorite car? ")
    return f"{color} {year} {make} {model}"



toAsk = ["food", "color", "animal", "movie", "song", "song artist", "book", "book author", "sport", "hobby", "place", "game", "car"]#list

name = input("What is your name? ")
print(f"Hello, {name}")
with open("Project 4/favorite items.txt", "w") as file:#create file and write user's name to it
    file.write(f"{name}'s favorite items:\n")

ask(toAsk)#call the ask function with the list of items to ask about

print()
with open("Project 4/favorite items.txt", "r") as file:#read the file and print it out
    print(file.read())