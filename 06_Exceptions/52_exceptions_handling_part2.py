# multiple exceptions can be handled together.(if we want to display exact same message)
# If we enter age as 0 (Zero) , we will get the error msg from the first exception ValueError.
# Since this exception gets handled in the first except block,
# the second except block will not be executed.
# Actually , if any exception is handled by the previous except block,
# then the remaining except blocks will not be executed. and the code after the try block
# will be executed...

try:
    age = int(input('Age: '))
    print(age)
    print("code is at point 1")
    income = 20000
    risk = income / age
    print(risk)
    print("code is at point 2")
except (ValueError, ZeroDivisionError):  #multiple types of exceptions,block executes if any 1 matches
    print("You didn't enter a valid age.")
except ValueError:                            # since ValueError exception is already handled above
    print("You didn't enter a valid age.")    # this will never get a chance to be executed
else:
    print("No exception were thrown")