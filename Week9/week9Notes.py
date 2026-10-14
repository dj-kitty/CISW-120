#learn how write read and edit files w/ python
#common modes when using files

# "r" read only
#you can only read but cant change it
#error if file doesnt exist

# "w" write
#Creates file if not existing
#Overwrites existing file

# "a" append
#creates file 
#adds new text at the end of the file and keeps old content

#with open("FOldername/filename", "mode") can use \\ instead of /
# with open("Week9/stuff.txt", "r") as file:
#     content = file.read()
#     print(content)


# with open("Week9/stuff.txt", "w") as file:
#     file.write(" This line is underneath")
# #when indentation is left, file automatically closes

#read method A: read whole file at once

# with open("Week9/stuff.txt", "r") as file:
#     contents = file.read
#     print(contents)

#read method B: read line by line using for loop

# with open("Week9/stuff.txt", "r") as file:
#     for line in file:
#         print(line)


#appending
#adds to end of file withou deleting old content

# with open("Week9/stuff.txt", "a") as file:
#     file.write("\nThis should apper at the very end, cause we used mode a")
#we use R to verify if file exists

