def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")
# these are referred as positional arguments, because the order in which they are given matters
greet_user("John", "Smith")
print("Finish")

# with keyword argument (parameter name followed by its value), the position doesnt matter
# here the order doesnt matter
# sometimes keyword arguments are used to make our code more readable/meaningful.
greet_user(last_name="Smith", first_name="John")

# calc_cost(50, 5, 0.1)
# the below is more readable
# calc_cost(total=50, shipping=5, discount=0.1)

# TIP 1: most of the time, use positional argument, but when a function call
# has lot of numeric values, then use keyword argument for better readability.
# Simply prefix the arguments with the name of their parameters

# TIP 2: if we are mixing positional and keyword arguments, then the positional arguments
# must come first before the keyword arguments, otherwise we get an error.
# greet_user(last_name="Smith", "John") -> this will give error
# greet_user("Smith", first_name="John") #-> this is also error
greet_user("John", last_name="Smith") # -> this is fine
