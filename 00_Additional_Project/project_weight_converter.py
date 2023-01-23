weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")

#weight = int(weight)
#unit = unit.upper()

if unit.upper() == 'L':
    converted_weight = int(weight) * 0.45
    print(f"You are {converted_weight} kilos")
elif unit.upper() == 'K':
    converted_weight = int(weight) / 0.45
    print(f"You are {converted_weight} pounds")