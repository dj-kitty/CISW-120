import time

timer = int(input("How many seconds do you want to count down from? "))

if timer < 0:
    print("Invalid time")
    timer = int(input("How many seconds do you want to count down from? "))

while timer >= 0:
    print(timer)
    if timer == 3:
        print("Almost there!")
    if timer == 0:
        print("Time's up!")
        break
    timer -= 1
    time.sleep(1)