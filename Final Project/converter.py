def convert_temp():

    value = int(input("Please input the temperature to convert.  "))
    units = input("What are the units of the temperature? (C for Celsius, F for Fahrenheit, K for Kelvin)  ").upper()
    new_units = input("What do you want to convert it to? (C for Celsius, F for Fahrenheit, K for Kelvin)  ").upper()

    x = value

    temp_convert_factors = {
        "CtoF": x * (9/5) + 32 + " degrees Fahrenheit",
        "FtoC": (x - 32) * (5/9) + " degrees Celsius",
        "CtoK": (x + 273.15) + " Kelvin", 
        "KtoC": (x - 273.15) + " degrees Celsius", 
        "KtoF": x * (9/5) - 459.67 + " degrees Fahrenheit", 
        "FtoK": (x + 459.67) * (5/9) + " Kelvin"
    }

    conversion = (f"{units}to{new_units}")

    factor = temp_convert_factors[conversion]

    return(factor)


def convert_weight():

    value = int(input("What value would you like to convert?  "))
    units = input("Is your mass in SI units or US Customary units? (SI or US)  ").upper()
    if units =="SI":
        to_change = input("Do you want to stay in grams or convert to pounds? (grams or pounds)  ").lower()

        if to_change == "grams":
            base = convert_prefixes(value, True)
            print(f"Converted weight: {base}g ")
        else:
            base = convert_prefixes(value, False)

            lbs = value / 453.6

            new_unit = input("What unit would you like to be in? (lbs, ozs, or tons)  ").lower()

            if new_unit == "lbs":
                print(f"Converted weight: {lbs} lbs")
            else:
                print(convert_pounds(lbs, False))



    elif units == "US":
        to_change = input("Do you want to stay in pounds or convert to grams? (grams or pounds)  ").lower()

        if to_change == "pounds":
            print(convert_pounds(value, True))
        else:
            converted = convert_pounds(value, False)
            grams = value * 453.6
            final_value = convert_prefixes(grams, True)
            print(f"Converted weight: {final_value}g ")


def convert_prefixes(x, change):


    to_base = {
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

    from_base = {
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


    base = to_base[prefix]

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

        new_value = from_base[prefix]
        return (f"{new_value} {prefix}")


def convert_pounds(x, change):

    factors = {
        "ton": 2000 * x,
        "oz": x/16
    }

    to_lbs_from = {
        "ton": x/2000,
        "oz": x * 16
    }

    if change != True:

        new_unit = input("Would you like to convert to oz or tons? (oz or ton)  ").lower()

        x = factors[new_unit]
        return (f"{x} {new_unit}")

    elif change == True:
        current_unit = input("What unit are you currently in: oz, pounds, or tons? (oz, lbs, tons)  ").lower()
        new_unit = input("What unit would you like to be in? (oz, lbs, tons)  ").lower()

        if current_unit != "lbs":
            x = factors[current_unit]
        else:
            x = x

        if new_unit == "lbs":
            return (f"{x} lbs")
        else:
            x = to_lbs_from[new_unit]
            return (f"{x} {new_unit}")


def convertLength():

    length = int(input("What length would you like to convert?  "))
    units = input("Is your length in SI units or US Customary units? (SI or US)  ").upper()

    if units == "SI":
        to_change = input("Do you want to stay in meters or convert to feet? (meters or feet)  ").lower()

        if to_change == "meters":
            base = convert_prefixes(length, True)
            print(f"Converted length: {base}m ")
        else:
            base = convert_prefixes(length, False)

            feet = length * 3.281

            new_unit = input("What unit would you like to be in? (ft, in, yd, or mi)  ").lower()

            if new_unit == "ft":
                print(f"Converted length: {feet} ft")
            else:
                print(convert_feet(feet, False))
    elif units == "US":
        to_change = input("Do you want to stay in feet or convert to meters? (meters or feet)  ").lower()

        if to_change == "feet":
            print(convert_feet(length, True))
        else:
            converted = convert_feet(length, False)
            meters = length / 3.281
            final_value = convert_prefixes(meters, True)
            print(f"Converted length: {final_value}m ")


def convert_feet(x, change):

    factors = {
        "in": x * 12,
        "yd": x / 3,
        "mi": x / 5280
    }

    to_feet_from = {
        "in": x / 12,
        "yd": x * 3,
        "mi": x * 5280
    }

    if change != True:

        new_unit = input("Would you like to convert to in, yd, or mi? (in, yd, mi)  ").lower()

        x = factors[new_unit]
        return (f"{x} {new_unit}")

    elif change == True:
        current_unit = input("What unit are you currently in: in, ft, yd, or mi? (in, ft, yd, mi)  ").lower()
        new_unit = input("What unit would you like to be in? (in, ft, yd, mi)  ").lower()

        if current_unit != "ft":
            x = factors[current_unit]
        else:
            x = x

        if new_unit == "ft":
            return (f"{x} ft")
        else:
            x = to_feet_from[new_unit]
            return (f"{x} {new_unit}")


def convert_speed():

    speed = int(input("What speed would you like to convert?  "))
    units = input("Is your speed in SI units or US Customary units? (SI or US)  ").upper()  

    if units == "SI":

        distance = input("Is your speed measured in meters or kilometers? (m or km)  ").lower()
        time = input("Is your speed measured in seconds or hours? (s or h)  ").lower()

        


# def convertArea():

# def convertVolume():

