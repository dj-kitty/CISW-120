signalColor=input("What color is the traffic light? ").lower()
isBlinking = input("Is the light blinking? ").lower()
if signalColor == "red":
    if isBlinking == "yes":
        print("This is now a 4-way stop. ")
    else:
        print("Stop")
elif signalColor == "yellow":
    if isBlinking == "yes":
        print("Proceed with caution.")
    else:
        print("Slow down.")
elif signalColor == "green":
    print("Go!")
else:
    print("You should get your vision checked.")