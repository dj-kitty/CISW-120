# # lists are storing multiple values in order
# favgames = ["minecraft", "another", "another1"]
# # print(favgames[0])
# # print(favgames[1])
# # print(favgames[2])

# #use len() to fing number of items in list
# print(len(favgames))

# #append() adds items to list
# favgames.append("yetanother")

# #inserting with insert()
# favgames.insert(1, "game")

# print(favgames)

# #commmonmethods
# #count(), counts number of repetitions
# #remove
# #sort(), 
# #reverse(), reverses order of list

# favgames.reverse()
# print(favgames)

# #loop through items in list?

# for games in favgames:
#     print(games)




#Dictionaries




#stores labeled info
#stores data in key value pairs
#are useful when label matters more than position

#make a dictionary called playerStats

playerStats = {
    #values must be health, mana, level, gold
#word: value      setup of information
    "Health": 100,
    "Mana": 40,
    "Level": 15,
    "Gold": 25

}


#list vs dictionary
#list matters when you want a collection of items
#dictionary is used when labels matter and you want to look things up by name









#accessing dictionary
# print(playerStats["health"])


#add an updated dictionary value?
#can add new key value pair by assigning value to new key
#you can also update/incread existing value


# playerStats["Strength"] = 15

# playerStats["Health"] = 200
# playerStats["Health"] += 50

# print(playerStats)


#keys() and values()

#keys() shows all keys
#values() shows all values

# print(playerStats.keys())
# print(playerStats.values())


#how we van loop through dictionaries
#we can loop through keys, values, or both
#items() is the most readable way to show evrythng in dictionary


#loop through keys

# for key in playerStats.keys():
#     print(key)


# #loop through values

# for value in playerStats.values():
#     print(value)


# #print both at the same time side by side

# for stats, values in playerStats.items():
#     print(f"{stats}, {values}")


#nested dictionary

students = {
    "001": {
        "Name": "Anna",
        "Major": "Programming",
        "Credits": "6"
    },
    "002": {
        "Name": "Joe",
        "Major": "Cyber",
        "Credits": "15"
        }
}


#how to access nested dictionary values???

#to do that, go one level at a time
#like file directories

# print(students["002"]["Major"])



#nested structures can mix lists and lictionaries
#programs often combine multiple data structures together
# inner dictionary can have a list as a value

students = {
    "005": {
        "Name": "Sebastian",
        "Classes": ["Math", "Hacking", "Linux"],
        "GPA": 2.8
    },

}