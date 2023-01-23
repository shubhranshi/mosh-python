# Magic methods in python start and end with '__'
# Magic methods are called automatically by python interpreter depending upon
# how we use our objects and classes.

# For eg. we do not call the __init__ method, it is called automatically by
# python interpreter when we create a new Point object.

# Complete list of python magic methods online: https://rszalski.github.io/magicmethods/

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):  # This method is returning our point as a string
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)

# if we do not implement __str__ method in our code, we get a default output that
# contains the memory address of that object.
# if we provide an implementation of __str__ method, then our defined message will
# be the output
print(point)

print(str(point))

# __str__ is same as the str() in-built function in python
# because of this implementation, both the print statements give the same output.
