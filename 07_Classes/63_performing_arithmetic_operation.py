# We also have magic methods for performing arithmetic operations between 2 objects.
# For eg. to add 2 objects

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)    # returns a new point object


point_1 = Point(100, 200)
point_2 = Point(200, 500)


print(point_1 + point_2)
# If don't implement the magic method "__add__" for + we will get an error
# TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
# And if we don't have the "__str__" magic method implemented
# we will see the new point object memory address

point_3 = point_1 + point_2
print(point_3.x)    # output 300, which proves that we successfully implemented __add__ method