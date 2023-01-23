x = 10
y = 11

# swap these 2 variables

z = x
x = y
y = x

print("x", x)
print("y", y)

# in python, we can swap without using a 3rd variable
x, y = y, x

print("x", x)
print("y", y)

# EXPLANATION:
# this is similar to
a, b = 1, 2 # right hand side is a tuple
# first we are defining a tuple 1, 2 and then we are unpacking it in a, b
