# We have 2 types of functions:
# 1 - Perform a task eg, print function and the above greet function
# 2 - Return a value eg, round function and below get_greeting function

# type 1
def greet(name):
    print(f"Hi {name}")


# type 2
def get_greet(name):
    return f"Hey {name}"


greet("Groot")
message = get_greet("Rocket")


# which of the two approach is better?
# the first one prints the output to the terminal
# in the 2nd one, we get the output in a variable, now we can use this
# value anywhere else in the code.

# for eg, writing the message into the file
file = open("../content.txt", "w")
file.write(message)
