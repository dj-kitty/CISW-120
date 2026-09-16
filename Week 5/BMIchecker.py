weight = float(input("What is you weight in pounds? "))
feet = int(input("How tall are you in feet? "))
inches = int(input("How many inches taller than that foot measurement are you? "))

height = (feet * 12) + inches #get total height in inches

BMI = (weight/height**2) * 703 #finding BMI

print(f"Your BMI is {BMI}")

if BMI < 18.5:
    print("You are underweight.")
elif BMI < 25:
    print("You are in the optimal BMI range. Good job!!")
elif BMI < 30:
    print("You are overweight.")
else:
    print("You are obese.")