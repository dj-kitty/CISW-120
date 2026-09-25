price = float(input("What is the total price of the item(s) you are buying? "))
print("What state are you in? (Enter the two-letter abbreviation, e.g., 'CA' for California). ")
state = input("If you live in the District of Columbia, enter 'DC', and if you live in Puerto Rico, enter 'PR': ").upper()

if state == "AL": #determining the tax rate based on the state entered by the user
    taxRate = 0.04
elif state == "AK":
    taxRate = 0.00
elif state == "AZ":
    taxRate = 0.056
elif state == "AR":
    taxRate = 0.065
elif state == "CA":
    taxRate = 0.0725
elif state == "CO":
    taxRate = 0.029
elif state == "CT":
    taxRate = 0.0635
elif state == "DC":
    taxRate = 0.06
elif state == "DE":
    taxRate = 0.00
elif state == "FL":
    taxRate = 0.06
elif state == "GA":
    taxRate = 0.04
elif state == "HI":
    taxRate = 0.04
elif state == "ID":
    taxRate = 0.06
elif state == "IL":
    taxRate = 0.0625
elif state == "IN":
    taxRate = 0.07
elif state == "IA":
    taxRate = 0.06
elif state == "KS":
    taxRate = 0.065
elif state == "KY":
    taxRate = 0.06
elif state == "LA":
    taxRate = 0.0445
elif state == "ME":
    taxRate = 0.055
elif state == "MD":
    taxRate = 0.06
elif state == "MA":
    taxRate = 0.0625
elif state == "MI":
    taxRate = 0.06
elif state == "MN":
    taxRate = 0.06875
elif state == "MS":
    taxRate = 0.07
elif state == "MO":
    taxRate = 0.04225
elif state == "MT":
    taxRate = 0.00
elif state == "NE":
    taxRate = 0.055
elif state == "NV":
    taxRate = 0.0685
elif state == "NH":
    taxRate = 0.00
elif state == "NJ":
    taxRate = 0.06625
elif state == "NM":
    taxRate = 0.05125
elif state == "NY":
    taxRate = 0.04
elif state == "NC":
    taxRate = 0.0475
elif state == "ND":
    taxRate = 0.05
elif state == "OH":
    taxRate = 0.0575
elif state == "OK":
    taxRate = 0.045
elif state == "OR":
    taxRate = 0.00
elif state == "PA":
    taxRate = 0.06
elif state == "PR":
    taxRate = 0.105
elif state == "RI":
    taxRate = 0.07
elif state == "SC":
    taxRate = 0.06
elif state == "SD":
    taxRate = 0.045
elif state == "TN":
    taxRate = 0.07
elif state == "TX":
    taxRate = 0.0625
elif state == "UT":
    taxRate = 0.0485
elif state == "VT":
    taxRate = 0.06
elif state == "VA":
    taxRate = 0.053
elif state == "WA":
    taxRate = 0.065
elif state == "WV":
    taxRate = 0.06
elif state == "WI":
    taxRate = 0.05
elif state == "WY":
    taxRate = 0.04
else:
    print("Sorry, that does not appear to be a state. Please try again.")

taxAmount = price * taxRate
totalPrice = price + taxAmount

print(f"Your state has a tax rate of {taxRate}. This means your cost after tax is {totalPrice}.")

isMember = input("Are you a member of our store? (Enter 'yes' or 'no'): ").lower() #if someone is a member, they will receive an additional 5% discount on the total price after tax 
if isMember == "yes":
    memberDiscountRate = 0.05
    discount = 0.05
    percentDiscount = str(discount * 100) + "%"
    
if totalPrice >= 100: #discounts based on the total price after tax
    discountRate = 0.10
    if isMember == "yes":
        discountRate += memberDiscountRate
    percentDiscount = str(discountRate * 100) + "%"
    print(f"You have received a {percentDiscount} discount.")
elif totalPrice >= 200:
    discountRate = 0.15
    if isMember == "yes":
        discountRate += memberDiscountRate
    percentDiscount = str(discountRate * 100) + "%"
    print(f"You have received a {percentDiscount} discount.")
elif totalPrice >= 300:
    discountRate = 0.20
    if isMember == "yes":
        discountRate += memberDiscountRate
    percentDiscount = str(discountRate * 100) + "%"
    print(f"You have received a {percentDiscount} discount.")

discountAmount = totalPrice * discountRate
totalPrice -= discountAmount


print(f"The total price after tax and any applicable discounts is: ${totalPrice:.2f}.")