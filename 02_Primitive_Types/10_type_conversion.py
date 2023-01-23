birth_year = input('Birth Year: ')  # Even if the input is a number it will be read as a string
print(type(birth_year))
age = 2022 - int(birth_year)    # need to convert string to int
print(type(age))
print(age)

weight_pound = input('Enter weight in pound: ')
kg_pound = int(weight_pound) * 0.45
print('Kilogram ' + str(kg_pound))


# type converters
# int() converts to an integer

# float() converts to float

# bool() converts to boolean

# Falsy values - values that return False
# boolean values that are considered as False: 0, None, ""
# boolean considers all other values as True

print(bool(0))          # False
print(bool(-10))        # True
print(bool(""))         # False
print(bool("False"))    # True
print(bool(None))       # False
print(bool(5))          # True


