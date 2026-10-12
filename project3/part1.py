#This is a countdown timer program. The user inputs the number of hours, minutes and seconds, and the computer converts it all to seconds
#and counts down and prints each remaining time. For specific times, it will print a message to the user. When the timer reaches 0, it will print "Time's up!" and end the program.
#Created by David Johnson for Intro to Programming


import time

hours = int(input("How many hours do you want to count down from? "))
minutes = int(input("How many minutes? "))
seconds = int(input("How many seconds? "))

total_seconds = hours * 3600 + minutes * 60 + seconds

while total_seconds >= 0:
    hours = total_seconds // 3600 #use floor division to get the number of hours
    minutes = (total_seconds % 3600) // 60 #use remainder division to get the number of partial hours and then floor division to get the number of minutes
    seconds = total_seconds % 60 #use remainder division to get the number of seconds

    if minutes == 0 and seconds == 0:
        if hours == 0:
            print("Time's up!")
        else:
            print(f"{hours:02d} hours remaining")

    elif hours == 0 and minutes == 30 and seconds == 0:
        print(f"{minutes:02d} minutes remaining")

    elif hours == 0 and minutes == 15 and seconds == 0:
        print(f"{minutes:02d} minutes remaining")

    elif hours == 0 and minutes == 10 and seconds == 0:
        print(f"{minutes:02d} minutes remaining")

    elif hours == 0 and minutes == 5 and seconds == 0:
        print(f"{minutes:02d} minutes remaining")

    elif hours == 0 and minutes == 1 and seconds == 0:
        print(f"{minutes:02d} minutes remaining")

    elif hours == 0 and minutes == 0 and seconds == 30:
        print(f"{seconds:02d} seconds remaining")

    elif hours == 0 and minutes == 0 and seconds == 10:
        print(f"{seconds:02d} seconds remaining")

    elif hours == 0 and minutes == 0 and seconds == 5:
        print("Almost there!")

    else:
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    time.sleep(1)
    total_seconds -= 1