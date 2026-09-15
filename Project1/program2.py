element = input("What is the name of the element? ")
moles = float(input(f"How many moles of {element} do you have? "))
molarMass = float(input(f"Enter the molar mass of {element} (g/mol). This is the same thing as the atomic mass unit of the element. "))
mass = moles * molarMass#finds the total mass of the element

AvogadroNumber = 6.02e23#this method of exponents, the power of ten, was learned from W3Schools, https://www.w3schools.com/python/python_numbers.asp
numberOfAtoms = moles * AvogadroNumber#Avogadro's number is the number of atoms in one mole of a substance, so this finds the total number of atoms in the given moles of the element

print(f"{moles} moles of {element} has a mass of about {mass} grams and contains {numberOfAtoms} atoms.")