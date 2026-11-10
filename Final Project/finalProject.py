def convertTemp():

    value = int(input("Please input the temperature to convert.  "))
    units = input("What are the units of the temperature? (C for Celsius, F for Fahrenheit, K for Kelvin)  ").upper()
    newUnits = input("What do you want to convert it to? (C for Celsius, F for Fahrenheit, K for Kelvin)  ").upper()

    x = value

    tempConvertFactors = {
        "CtoF": x * (9/5) + 32,
        "FtoC": (x - 32) * (5/9),
        "CtoK": (x + 273.15), 
        "KtoC": (x - 273.15), 
        "KtoF": x * (9/5) - 459.67, 
        "FtoK": (x + 459.67) * (5/9)
    }

    conversion = (f"{units}to{newUnits}")

    factor = tempConvertFactors[conversion]

    return(factor)


def convertWeight():

    value = int(input("What value would you like to convert?  "))
    units = input("Is your mass in SI units or US Customary units? (SI or US)  ").upper()
    toChange = input("Do you want to change the type of unit to a different type or a different factor? (type or factor)").lower()

    if toChange == "factor":
        base = convertSIPrefixes(value, True)


def convertSIPrefixes(value, change):

    if change == True:
        print("What is the prefix on your unit?")
        print("1: T")
        print("2: G")
        print("3: M")
        print("4: K")
        print("5: da")
        print("6: none")
        print("7: d")
        print("8: c")
        print("9: m")
        print("10: µ")
        print("11: n")
        print("12: T")
        print("13: none")        
        prefix = input("")


    x = value

    factors = {
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

# def convertLength():

# def convertSpeed():

# def convertArea():

# def convertVolume():
