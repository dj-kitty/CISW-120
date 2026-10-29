
def ask(list):
    for item in list:
        answer = input(f"What is your favorite {item}? ")
        if item == "car":
            answer = askCar()
        with open("Project 4/favorite items.txt", "a") as file:
            file.write(f"{item}: {answer}\n")

def askCar():
    make = input("What is the make of your favorite car? ")
    model = input("What is the model of your favorite car? ")
    year = input("What is the year of your favorite car? ")
    color = input("What is the color of your favorite car? ")
    return f"{color} {year} {make} {model}"





toAsk = ["food", "color", "animal", "movie", "song", "song artist", "book", "book author", "sport", "hobby", "place", "game", "car"]

name = input("What is your name? ")
with open("Project 4/favorite items.txt", "w") as file:
    file.write(f"{name}'s favorite items:\n")