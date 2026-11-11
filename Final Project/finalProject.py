def convertTemp():

    value = int(input("Please input the temperature to convert.  "))
    units = input("What are the units of the temperature? (C for Celsius, F for Fahrenheit, K for Kelvin)  ").upper()
    newUnits = input("What do you want to convert it to? (C for Celsius, F for Fahrenheit, K for Kelvin)  ").upper()

    x = value

    tempConvertFactors = {
        "CtoF": x * (9/5) + 32 + " degrees Fahrenheit",
        "FtoC": (x - 32) * (5/9) + " degrees Celsius",
        "CtoK": (x + 273.15) + " Kelvin", 
        "KtoC": (x - 273.15) + " degrees Celsius", 
        "KtoF": x * (9/5) - 459.67 + " degrees Fahrenheit", 
        "FtoK": (x + 459.67) * (5/9) + " Kelvin"
    }

    conversion = (f"{units}to{newUnits}")

    factor = tempConvertFactors[conversion]

    return(factor)


def convertWeight():

    value = int(input("What value would you like to convert?  "))
    units = input("Is your mass in SI units or US Customary units? (SI or US)  ").upper()
    if units =="SI":
        toChange = input("Do you want to stay in grams or convert to pounds? (grams or pounds)  ").lower()

        if toChange == "grams":
            base = convertPrefixes(value, True)
            print(f"Converted weight: {base}g ")
        else:
            base = convertPrefixes(value, False)

            lbs = value / 453.6

            newUnit = input("What unit would you like to be in? (lbs, ozs, or tons)  ").lower()

            if newUnit == "lbs":
                print(f"Converted weight: {lbs} lbs")


    elif units == "US":
        toChange = input("Do you want to stay in pounds or convert to grams? (grams or pounds)  ").lower()


    

def convertPrefixes(value, change):

    x = value

    toBase = {
        "T": x * 10**12,
        "G": x * 10**9,
        "M": x * 10**6,
        "K": x * 1000,
        "da": x * 100,
        "h": x * 10,
        "d": x / 10,
        "c": x / 100,
        "m": x / 1000,
        "µ": x / 10**6,
        "n": x / 10**9,
        "p": x / 10**12
    }

    fromBase = {
        "T": x / 10**12,
        "G": x / 10**9,
        "M": x / 10**6,
        "K": x / 1000,
        "da": x / 100,
        "h": x / 10,
        "d": x * 10,
        "c": x * 100,
        "m": x * 1000,
        "µ": x * 10**6,
        "n": x * 10**9,
        "p": x * 10**12
    }

    print("What is the prefix on your unit?")
    print("1: T")
    print("2: G")
    print("3: M")
    print("4: K")
    print("5: da")
    print("6: h")
    print("7: none (base)")
    print("8: d")
    print("9: c")
    print("10: m")
    print("11: µ")
    print("12: n")
    print("13: p")        
    prefix = input("Please enter the prefix:  ")


    base = toBase[prefix]

    if change != True:
        return (base)
    elif change == True:
        print("What prefix do you want on your value?")
        print("1: T")
        print("2: G")
        print("3: M")
        print("4: K")
        print("5: da")
        print("6: h")
        print("7: none (base)")
        print("8: d")
        print("9: c")
        print("10: m")
        print("11: µ")
        print("12: n")
        print("13: p")        
        prefix = input("Please enter the prefix:  ")

        newValue = fromBase[prefix]
        return (f"{newValue} {prefix}g")
        
def convertPounds(value, change, unit):

    x = value





# def convertLength():

# def convertSpeed():

# def convertArea():

# def convertVolume():