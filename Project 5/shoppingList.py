#This prrgram hast eh user create a shopping list and saves it to the file. If that file already has a list in it, it will load that
#list to a regular list
#Then the user has the option to add/remove items, sort the list, view the list, or clear the list. When the user exits, it will save
#  the list to the file.
#Created by David Johnson for Intro to Programming


with open("Project 5/shoppingList.txt", "r") as file:
    items = file.readlines() #since when the list is saved to this file, the items will be on separate lines
shoppingList = [items]#the list



def add_item(item):
    shoppingList.append(item) #add
    print(f"{item} added to the shopping list.")

def remove_item(item):
    if item in shoppingList:
        shoppingList.remove(item) #remove
        print(f"{item} removed from the shopping list.")
    else:
        print(f"{item} not found in the shopping list.")

def sort_list():
    shoppingList.sort() #sort
    print("Shopping list sorted.")

def view_list(): #see the list
    if shoppingList:
        print("Shopping List:")
        for item in shoppingList:
            print(f"- {item}")
    else:
        print("The shopping list is empty.")

def clear_list(): #delete all items from the list
    shoppingList.clear()
    print("Shopping list cleared.")

def run():
    print("Options:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Sort list")
    print("5. Clear list")
    print("6. Exit")

    while True:
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_item(item)
        elif choice == '3':
            view_list()
        elif choice == '4':
            sort_list()
        elif choice == '5':
            clear_list()
        elif choice == '6':
            print("Exiting the program.")

            with open("Project 5/shoppingList.txt", "w") as file:
                for item in shoppingList:
                    file.write(f"{item}\n") #save the list to the file when the user exits

            break
        else:
            print("Invalid choice. Please try again.")


run()
