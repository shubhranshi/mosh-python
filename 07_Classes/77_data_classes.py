from collections import namedtuple

# We use classes to bundle data and functionalities into one unit.
# In some cases we may come across with classes that don't have any behavior like functions.
# And only have data.

# Like in this example
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# With this we can create point objects
p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2) # This will return False, if __eq__ is not implemented
# because the two objects are stored in different locations of the memory
# It will return True if __eq__ is implemented

# To see where the objects are stored in memory use the "id()" functions that returns memory address.
print(id(p1))
print(id(p2))

# To solve this issue we must implement a magic method
# like the ones seen on lesson 08 Performing Arithmetic Operations.

# When dealing with classes that have no behavior, and just have data,
# whe can use namedtuple instead.
# Importing form the "collection" module the "namedtuple()" function

# The first argument we specify the label for the new type(class) we want to create.
# The second argument we pass an array of field names or attribute names.
Point_t = namedtuple("MyPoint", ["x", "y"])
p3 = Point_t(x=2, y=5)      # we have to use keyword arguments here.
p4 = Point_t(x=2, y=5)
p5 = Point_t(x=4, y=10)
print(p3 == p4)
print(p4 == p5)
print(p3)
print(p3.x)

# If working with classes, that only contain data it is usual better to use "namedtuple()"
# Our code is more clear and less ambiguous.
# And also that we do not ness to create a magic method to compare two objects.
# Just be aware that these namedtuple() are immutable, which means that the attributes
# cannot be modified after they are initialized.
